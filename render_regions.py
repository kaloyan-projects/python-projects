bl_info = {
    "name": "Render Frame Splits",
    "author" : "Kaloyan Ivanov",
    "blender": (4, 2, 0),
    "category": "Render",
    "description": "Split render into exact regions",
    "warning": "I don't know bpy that well"
}

import bpy

class RenderLeftThird(bpy.types.Operator):
    bl_idname = "render.left_third"
    bl_label = "Render Left Third"

    def execute(self, context):
        context.scene.render.border_min_x = 0
        context.scene.render.border_max_x = 1/3
        
        context.scene.render.border_min_y = 0
        context.scene.render.border_max_y = 1
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderMiddleThird(bpy.types.Operator):
    bl_idname = "render.middle_third"
    bl_label = "Render Middle Third"

    def execute(self, context):
        context.scene.render.border_min_x = 1/3
        context.scene.render.border_max_x = 2/3
        
        context.scene.render.border_min_y = 0
        context.scene.render.border_max_y = 1
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderRightThird(bpy.types.Operator):
    bl_idname = "render.right_third"
    bl_label = "Render Right Third"

    def execute(self, context):
        context.scene.render.border_min_x = 2/3
        context.scene.render.border_max_x = 1
        
        context.scene.render.border_min_y = 0
        context.scene.render.border_max_y = 1
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderTopThird(bpy.types.Operator):
    bl_idname = "render.top_third"
    bl_label = "Render Top Third"

    def execute(self, context):
        context.scene.render.border_min_x = 0
        context.scene.render.border_max_x = 1
        
        context.scene.render.border_min_y = 1
        context.scene.render.border_max_y = 2/3
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderMiddleThirdH(bpy.types.Operator):
    bl_idname = "render.middle_third_h"
    bl_label = "Render Middle Third"

    def execute(self, context):
        context.scene.render.border_min_x = 0
        context.scene.render.border_max_x = 1
        
        context.scene.render.border_min_y = 2/3
        context.scene.render.border_max_y = 1/3
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderBottomThird(bpy.types.Operator):
    bl_idname = "render.bottom_third"
    bl_label = "Render Bottom Third"

    def execute(self, context):
        context.scene.render.border_min_x = 0
        context.scene.render.border_max_x = 1
        
        context.scene.render.border_min_y = 1/3
        context.scene.render.border_max_y = 0
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderLeftHalf(bpy.types.Operator):
    bl_idname = "render.left_half"
    bl_label = "Render Left Half"

    def execute(self, context):
        context.scene.render.border_min_x = 0
        context.scene.render.border_max_x = 1/2
        
        context.scene.render.border_min_y = 0
        context.scene.render.border_max_y = 1
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderRightHalf(bpy.types.Operator):
    bl_idname = "render.right_half"
    bl_label = "Render Right Half"

    def execute(self, context):
        context.scene.render.border_min_x = 1/2
        context.scene.render.border_max_x = 1
        
        context.scene.render.border_min_y = 0
        context.scene.render.border_max_y = 1
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderTopHalf(bpy.types.Operator):
    bl_idname = "render.top_half"
    bl_label = "Render Top Half"

    def execute(self, context):
        context.scene.render.border_min_x = 0
        context.scene.render.border_max_x = 1
        
        context.scene.render.border_min_y = 1/2
        context.scene.render.border_max_y = 1
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderBottomHalf(bpy.types.Operator):
    bl_idname = "render.bottom_half"
    bl_label = "Render BottomHalf"

    def execute(self, context):
        context.scene.render.border_min_x = 0
        context.scene.render.border_max_x = 1
        
        context.scene.render.border_min_y = 0
        context.scene.render.border_max_y = 1/2
        context.scene.render.use_border = True
        return {'FINISHED'}

class RenderSplitPanel(bpy.types.Panel):
    bl_label = "Render Frame Splits"
    bl_idname = "RENDER_PT_frame_splits"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"

    def draw(self, context):
        layout = self.layout
        row_1 = layout.row()
        row_1.label(text="Thirds")
        layout.operator("render.left_third", text="Render Left Third")
        layout.operator("render.middle_third", text="Render Middle Third")
        layout.operator("render.right_third", text="Render Right Third")
        layout.row()
        layout.operator("render.top_third", text="Render Top Third")
        layout.operator("render.middle_third_h", text="Render Middle Third")
        layout.operator("render.bottom_third", text="Render Bottom Third")
        row_2 = layout.row()
        row_2.label(text="Halfs")
        layout.operator("render.left_half", text="Render Left Half")
        layout.operator("render.right_half", text="Render Right Half")
        layout.row()
        layout.operator("render.top_half", text="Render Top Half")
        layout.operator("render.bottom_half", text="Render Bottom Half")

def register():
    bpy.utils.register_class(RenderLeftThird)
    bpy.utils.register_class(RenderMiddleThird)
    bpy.utils.register_class(RenderRightThird)
    bpy.utils.register_class(RenderSplitPanel)
    bpy.utils.register_class(RenderLeftHalf)
    bpy.utils.register_class(RenderRightHalf)
    bpy.utils.register_class(RenderTopThird)
    bpy.utils.register_class(RenderMiddleThirdH)
    bpy.utils.register_class(RenderBottomThird)
    bpy.utils.register_class(RenderTopHalf)
    bpy.utils.register_class(RenderBottomHalf)

def unregister():
    bpy.utils.unregister_class(RenderLeftThird)
    bpy.utils.unregister_class(RenderMiddleThird)
    bpy.utils.unregister_class(RenderRightThird)
    bpy.utils.unregister_class(RenderSplitPanel)
    bpy.utils.unregister_class(RenderLeftHalf)
    bpy.utils.unregister_class(RenderRightHalf)
    bpy.utils.unregister_class(RenderTopThird)
    bpy.utils.unregister_class(RenderMiddleThirdH)
    bpy.utils.unregister_class(RenderBottomThird)
    bpy.utils.unregister_class(RenderTopHalf)
    bpy.utils.unregister_class(RenderBottomHalf)

if __name__ == "__main__":
    register()
