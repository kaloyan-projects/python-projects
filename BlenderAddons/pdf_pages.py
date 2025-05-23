bl_info = {
    "name": "PDF to Planes Importer",
    "author": "OpenAI",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "File > Import > PDF as Planes",
    "description": "Import a PDF file as image-textured planes",
    "category": "Import-Export",
}

import bpy
from bpy.types import Operator
from bpy.props import StringProperty, EnumProperty, IntProperty
from bpy_extras.io_utils import ImportHelper
import os
import tempfile
import fitz  # PyMuPDF
from mathutils import Vector

class IMPORT_OT_pdf_planes(Operator, ImportHelper):
    bl_idname = "import_scene.pdf_planes"
    bl_label = "Import PDF as Planes"
    bl_options = {'REGISTER', 'UNDO'}

    filename_ext = ".pdf"

    filter_glob: StringProperty(default="*.pdf", options={'HIDDEN'})

    layout_mode: EnumProperty(
        name="Layout",
        items=[
            ('GRID', "Grid", "Lay out pages in a grid"),
            ('STACK', "Stacked", "Stack pages like a book"),
        ],
        default='GRID'
    )

    dpi: IntProperty(
        name="DPI",
        description="Render resolution for each page",
        default=150,
        min=20,
        max=600
    )

    def execute(self, context):
        pdf_path = self.filepath
        layout = self.layout_mode
        dpi = self.dpi

        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            self.report({'ERROR'}, f"Failed to read PDF: {e}")
            return {'CANCELLED'}

        temp_dir = tempfile.mkdtemp(prefix="blender_pdf_")
        textures = []
        page_sizes = []

        self.report({'INFO'}, f"Rendering {len(doc)} pages...")

        # Convert each page to image and save
        for i, page in enumerate(doc):
            mat = fitz.Matrix(dpi / 72, dpi / 72)
            pix = page.get_pixmap(matrix=mat)
            img_path = os.path.join(temp_dir, f"page_{i + 1}.png")
            pix.save(img_path)
            textures.append(img_path)
            page_sizes.append((pix.width / dpi, pix.height / dpi))  # in inches, approx to Blender units

        doc.close()

        # Add planes with textures
        spacing = 0.5
        cols = int(len(textures) ** 0.5) + 1
        for idx, (img_path, (w, h)) in enumerate(zip(textures, page_sizes)):
            bpy.ops.mesh.primitive_plane_add(size=1)
            plane = context.active_object
            plane.name = f"PDF_Page_{idx+1}"
            plane.scale = Vector((w / 2, h / 2, 1))

            # Position plane
            if layout == 'GRID':
                row = idx // cols
                col = idx % cols
                plane.location = Vector(((w + spacing) * col, -(h + spacing) * row, 0))
            else:  # STACK
                plane.location = Vector((0, 0, -idx * 0.01))  # slight Z offset

            # Create and apply material
            mat = bpy.data.materials.new(name=f"PageMat_{idx+1}")
            mat.use_nodes = True
            bsdf = mat.node_tree.nodes.get("Principled BSDF")

            tex_image = mat.node_tree.nodes.new('ShaderNodeTexImage')
            tex_image.image = bpy.data.images.load(img_path)
            mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])

            plane.data.materials.append(mat)

        self.report({'INFO'}, "Import complete!")
        return {'FINISHED'}


def menu_func_import(self, context):
    self.layout.operator(IMPORT_OT_pdf_planes.bl_idname, text="PDF as Textured Planes (.pdf)")


def register():
    bpy.utils.register_class(IMPORT_OT_pdf_planes)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(IMPORT_OT_pdf_planes)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()
