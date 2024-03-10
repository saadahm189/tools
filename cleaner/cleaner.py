import os
import shutil
import tempfile
import ctypes
import ctypes.wintypes


def delete_files_in_temp_folders():
    temp_folders = [tempfile.gettempdir()]
    if os.name == "nt":  # If running on Windows, add the %temp% folder
        temp_folders.append(os.environ.get("TEMP", os.environ.get("TMP")))

    for temp_folder in temp_folders:
        print(f"Deleting contents in temp folder: {temp_folder}")
        try:
            for root, dirs, files in os.walk(temp_folder, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        print(f"Deleted file: {file_path}")
                    except Exception as e:
                        print(f"Could not delete file: {file_path} - {e}")

                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    try:
                        shutil.rmtree(dir_path)
                        print(f"Deleted directory: {dir_path}")
                    except Exception as e:
                        print(f"Could not delete directory: {dir_path} - {e}")

            print(f"All contents deleted from temp folder: {temp_folder}")

        except FileNotFoundError:
            print(f"Folder '{temp_folder}' not found.")
        except Exception as e:
            print(
                f"An error occurred while deleting contents in temp folder '{temp_folder}': {e}"
            )


def delete_contents_in_folders():
    try:
        for root, dirs, files in os.walk("C:\Windows\Temp", topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Could not delete file: {file_path} - {e}")

            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Deleted directory: {dir_path}")
                except Exception as e:
                    print(f"Could not delete directory: {dir_path} - {e}")

        print(f"All contents deleted from folder")

    except FileNotFoundError:
        print(f"Folder not found")
    except Exception as e:
        print(f"An error occurred while deleting contents in folder: {e}")


def empty_recycle_bin():
    SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
    SHEmptyRecycleBin.argtypes = [
        ctypes.wintypes.HWND,
        ctypes.wintypes.LPCWSTR,
        ctypes.wintypes.DWORD,
    ]
    SHEmptyRecycleBin.restype = ctypes.wintypes.LONG

    hwnd = None
    pszRootPath = None
    dwFlags = 0x1

    if SHEmptyRecycleBin(hwnd, pszRootPath, dwFlags) == 0:
        print("Recycle bin emptied successfully!")
    else:
        print("Failed to empty the recycle bin.")


if __name__ == "__main__":
    delete_files_in_temp_folders()
    delete_contents_in_folders()
    empty_recycle_bin()
