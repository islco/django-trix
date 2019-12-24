import os

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif'}


def is_valid_image_extension(file_path):
    extension = os.path.splitext(str(file_path).lower())[1]
    return extension in IMAGE_EXTENSIONS
