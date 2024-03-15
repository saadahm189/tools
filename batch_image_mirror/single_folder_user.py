import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os


def flip_images_in_folder(input_folder, output_folder):
    # Create the output folder and its parent directory if they don't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image
        if filename.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            # Open the image
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)

            # Flip the image horizontally
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

            # Save the flipped image to the output folder
            output_path = os.path.join(output_folder, filename)
            flipped_img.save(output_path)


def select_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_folder)


def select_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder)


def flip_images():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    flip_images_in_folder(input_folder, output_folder)
    tk.messagebox.showinfo("Success", "Images flipped successfully!")


# Create main window
root = tk.Tk()
root.title("Image Flipper")

# Input folder selection
input_folder_label = tk.Label(root, text="Input Folder:")
input_folder_label.grid(row=0, column=0, padx=5, pady=5)
input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1, padx=5, pady=5)
input_folder_button = tk.Button(root, text="Browse", command=select_input_folder)
input_folder_button.grid(row=0, column=2, padx=10, pady=5)

# Output folder selection
output_folder_label = tk.Label(root, text="Output Folder:")
output_folder_label.grid(row=1, column=0, padx=5, pady=5)
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=5, pady=5)
output_folder_button = tk.Button(root, text="Browse", command=select_output_folder)
output_folder_button.grid(row=1, column=2, padx=10, pady=5)

# Button to flip images
flip_button = tk.Button(root, text="Flip Images", command=flip_images)
flip_button.grid(row=2, column=1, padx=10, pady=10)

# Credit
new_name_label = tk.Label(root, text="Powered by Saad Ahmed")
new_name_label.grid(row=4, column=0)

# Run the main event loop
root.mainloop()
