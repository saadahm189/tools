from tkinter import Tk, Button, Label, filedialog, Entry
from PIL import Image, ExifTags
import os


def resize_images():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    target_resolution = (
        int(target_resolution_width_entry.get()),
        int(target_resolution_height_entry.get()),
    )

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)

    for file_name in files:
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        img = Image.open(input_path)

        if hasattr(img, "_getexif"):
            exif = img._getexif()
            if exif is not None:
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == "Orientation":
                        break
                if orientation in exif:
                    if exif[orientation] == 3:
                        img = img.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        img = img.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        img = img.rotate(90, expand=True)

        img.thumbnail(target_resolution, Image.LANCZOS)

        new_img = Image.new("RGB", target_resolution, (255, 255, 255))

        img_width, img_height = img.size
        new_img.paste(
            img,
            (
                (target_resolution[0] - img_width) // 2,
                (target_resolution[1] - img_height) // 2,
            ),
        )

        new_img.save(output_path)


def select_input_folder():
    folder_selected = filedialog.askdirectory()
    input_folder_entry.delete(0, "end")
    input_folder_entry.insert(0, folder_selected)


def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_entry.delete(0, "end")
    output_folder_entry.insert(0, folder_selected)


root = Tk()
root.title("Image Resizer")

input_folder_label = Label(root, text="Input Folder:")
input_folder_label.grid(row=0, column=0, padx=10, pady=10)
input_folder_entry = Entry(root, width=50)
input_folder_entry.grid(row=0, column=1, padx=10, pady=10)
input_folder_button = Button(root, text="Browse", command=select_input_folder)
input_folder_button.grid(row=0, column=2, padx=10, pady=10)

output_folder_label = Label(root, text="Output Folder:")
output_folder_label.grid(row=1, column=0, padx=10, pady=10)
output_folder_entry = Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=10, pady=10)
output_folder_button = Button(root, text="Browse", command=select_output_folder)
output_folder_button.grid(row=1, column=2, padx=10, pady=10)

target_resolution_label = Label(root, text="Target Resolution:")
target_resolution_label.grid(row=2, column=0, padx=10, pady=10)
target_resolution_width_entry = Entry(root, width=10)
target_resolution_width_entry.grid(row=2, column=1, padx=10, pady=10)
target_resolution_height_entry = Entry(root, width=10)
target_resolution_height_entry.grid(row=2, column=2, padx=10, pady=10)

resize_button = Button(root, text="Resize Images", command=resize_images)
resize_button.grid(row=3, columnspan=3)

root.mainloop()
