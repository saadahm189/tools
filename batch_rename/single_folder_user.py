import os
import tkinter as tk
from tkinter import filedialog


def rename_files(folder_path, new_name):
    files = os.listdir(folder_path)
    files.sort()
    for i, file_name in enumerate(files):
        base_name, extension = os.path.splitext(file_name)
        new_file_name = f"{new_name}-{i}{extension}"
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)
        os.rename(old_path, new_path)


def browse_folder():
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(tk.END, filedialog.askdirectory())


def rename():
    folder_path = folder_path_entry.get()
    new_name = new_name_entry.get()
    if not os.path.isdir(folder_path):
        result_label.config(text="Invalid folder path")
        return
    try:
        rename_files(folder_path, new_name)
        result_label.config(text="Files renamed successfully")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")


# Create GUI window
root = tk.Tk()
root.title("File Renamer")

# Folder path entry
folder_path_label = tk.Label(root, text="Folder Path:")
folder_path_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.grid(row=0, column=1, pady=10, padx=10)
folder_path_button = tk.Button(root, text="Browse File", command=browse_folder)
folder_path_button.grid(row=0, column=2, padx=10, pady=10)

# New name entry
new_name_label = tk.Label(root, text="New Name:")
new_name_label.grid(row=1, column=0, sticky="e")
new_name_entry = tk.Entry(root, width=50)
new_name_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to initiate renaming
rename_button = tk.Button(root, text="Rename", command=rename)
rename_button.grid(row=2, column=1, padx=15, pady=15)

# Label to show result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=1)

# Credit
new_name_label = tk.Label(root, text="Powered by Saad Ahmed")
new_name_label.grid(row=4, column=0)

# Start GUI
root.mainloop()
