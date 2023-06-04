import os
import shutil


def remove_all(folder_path):
    """
    Remove all file in folder_path
    :param folder_path:
    :return:
    """
    for i in os.listdir(folder_path):
        if i in [".git", "README.MD", "annotation.csv", "font_annotation.csv"]:
            continue

        file_path = os.path.join(folder_path, i)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def remove_position(folder_path, pos):
    """
    Remove file with position
    :param folder_path:
    :param pos:
    :return:
    """
    files_name = str(pos).zfill(5)
    os.remove(os.path.join(folder_path, files_name + ".png"))


def remove_all_in_folder(folder_path):
    """Remove all file in folder_path

    Args:
        folder_path (str): should be a folder path
    """
    remove_path = []

    if not os.listdir(folder_path):
        print(f"{folder_path} is empty")
        return

    for i in os.listdir(folder_path):
        remove_path.append(os.path.join(folder_path, i))

    # remove all file in folder_path
    for i in remove_path:
        if os.path.isfile(i):
            os.remove(i)
        elif os.path.isdir(i):
            shutil.rmtree(i)


if __name__ == "__main__":
    print("remove_all")
    remove_all("../../PimthaiGANS-Dataset/data")
    print("remove done")
