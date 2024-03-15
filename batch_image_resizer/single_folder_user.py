import tkinter as tk
from tkinter import filedialog
from PIL import Image, ExifTags
import os


def remove_exif_orientation(img):
    # Remove EXIF orientation metadata
    if hasattr(img, "_getexif"):
        exif = img._getexif()
        if exif is not None:
            for tag, value in exif.items():
                if tag in ExifTags.TAGS.keys() and ExifTags.TAGS[tag] == "Orientation":
                    img = apply_orientation(img, value)
    return img


def apply_orientation(img, orientation):
    if orientation == 1:
        return img
    elif orientation == 2:
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 3:
        return img.transpose(Image.ROTATE_180)
    elif orientation == 4:
        return img.transpose(Image.FLIP_TOP_BOTTOM)
    elif orientation == 5:
        return img.transpose(Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 6:
        return img.transpose(Image.ROTATE_270)
    elif orientation == 7:
        return img.transpose(Image.ROTATE_90).transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 8:
        return img.transpose(Image.ROTATE_90)
    else:
        return img


def resize_image(input_path, output_path, max_size_kb=500):
    # Open the image
    with Image.open(input_path) as img:
        # Remove EXIF orientation metadata
        img = remove_exif_orientation(img)

        # Calculate the aspect ratio
        aspect_ratio = img.width / img.height

        # Calculate new width and height to maintain aspect ratio
        new_width = int((max_size_kb * 1024) ** 0.5 * aspect_ratio)
        new_height = int(new_width / aspect_ratio)

        # Resize the image
        img = img.resize((new_width, new_height), Image.LANCZOS)

        # Save the resized image with desired compression quality
        img.save(output_path, optimize=True, quality=95)


def resize_images_in_folder(input_folder, output_folder, max_size_kb):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    num_images_processed = 0

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if (
            filename.endswith(".jpg")
            or filename.endswith(".jpeg")
            or filename.endswith(".png")
        ):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            # Resize the image
            resize_image(input_path, output_path, max_size_kb)
            num_images_processed += 1

    # Display complete message
    tk.messagebox.showinfo(
        "Complete", f"All {num_images_processed} images have been resized."
    )


def browse_button(entry):
    filename = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, filename)


def start_process():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    max_size_kb = int(max_size_entry.get())

    resize_images_in_folder(input_folder, output_folder, max_size_kb)


root = tk.Tk()
root.title("Image Resizer")

input_folder_label = tk.Label(root, text="Input Folder:")
input_folder_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1, padx=10, pady=10)
input_folder_button = tk.Button(
    root, text="Browse", command=lambda: browse_button(input_folder_entry)
)
input_folder_button.grid(row=0, column=2)

output_folder_label = tk.Label(root, text="Output Folder:")
output_folder_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=10, pady=10)
output_folder_button = tk.Button(
    root, text="Browse", command=lambda: browse_button(output_folder_entry)
)
output_folder_button.grid(row=1, column=2)

max_size_label = tk.Label(root, text="Max Image Size (KB):")
max_size_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
max_size_entry = tk.Entry(root, width=10)
max_size_entry.grid(row=2, column=1, padx=10, pady=10)

start_button = tk.Button(root, text="Start", command=start_process)
start_button.grid(row=3, columnspan=3, padx=10, pady=10)

root.mainloop()
