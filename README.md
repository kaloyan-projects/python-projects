# python-projects
Python programs for automating various tasks.

## List
### Standalone scripts
1. [Base Converter](base_converter.py) – Simple program for converting between bases.
2. [Letter Frequency Diagram](letter_frequency_diagram.py) – Provide path to a text file and get the frequency of each letter, along with a diagram.
3. [File date diagram](file_date_diagram.py) – Creates a diagram showing the frequency of file modifications over time.
4. [Shuffle video](shuffle_video.py) – Shuffles a video, along with the audio and saves it to a new file.
5. [Image-Text Converter](img_txt_converter.py) – Converts text to an image and an image to text.
6. [SRT to Bash](srt_to_bash.py) – Converts a subtitle file to a bash script that echoes lines to the terminal with the appropriate delay.
### Blender Addons
7. [Render Regions](BlenderAddons/render_regions.py) – Easly splits the frame into halfs and thirds for rendering separate regions.
8. [PDF to textured planes](BlenderAddons/pdf_pages.py) – Import PDF files as individual planes with the rasterized pages as textures.

## Run
### Standalone scripts
Open the terminal and cd into the directory where the scripts are saved. Run them with
```
python3 script_name.py
```
### Blender addons
Go to Edit > Preferences > Add-ons > Install from Disk… and navigate to the python file. Then, select "Install from disk".
