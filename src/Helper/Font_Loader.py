import os
from typing import List


def font_loader(font_folder_path: str) -> List[str]:
    """
    Load all font path in font_folder_path
    :param font_folder_path: should be a folder path contain .tff files
    :return: List of unique font path
    """
    font_folder = []

    for font_path in os.listdir(font_folder_path):
        if font_path.endswith(".ttf"):
            path = os.path.join(font_folder_path, font_path)
            font_folder.append(path)

    font_folder = set(font_folder)
    font_folder = list(font_folder)
    return font_folder
