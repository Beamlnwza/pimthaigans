import os


def folder_create(folder_path, number_of_folder=1):
    """
    Create folder in folder_path with number_of_folder
    :param folder_path:
    :param number_of_folder:
    :return:
    """
    nums = number_of_folder

    for i in range(nums):
        folder_name = f"{str(i).zfill(2)}"
        out_path = os.path.join(folder_path, folder_name)
        os.makedirs(out_path, exist_ok=True)


if __name__ == "__main__":
    print("Folder_Create")
    folder_create("../../PimthaiGANS-Dataset/data", 88)
    print("create done")
