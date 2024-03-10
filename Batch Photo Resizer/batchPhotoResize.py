from PIL import Image
import os


def resize_image(input_path, output_path, max_size_kb=500):
    # Open the image
    with Image.open(input_path) as img:
        # Calculate the aspect ratio
        aspect_ratio = img.width / img.height

        # Calculate new width and height to maintain aspect ratio
        new_width = int((max_size_kb * 1024) ** 0.5 * aspect_ratio)
        new_height = int(new_width / aspect_ratio)

        # Resize the image
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Save the resized image with desired compression quality
        img.save(output_path, optimize=True, quality=95)


def resize_images_in_folder(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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
            resize_image(input_path, output_path)


if __name__ == "__main__":
    input_folder = "Source_Folder"
    output_folder = "Destination_Folder"
    resize_images_in_folder(input_folder, output_folder)
