import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Plotter:
    def __init__(self, big_path, num_rows=8, num_cols=11, fig_size=(20, 28)):
        self.big_path = big_path
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.fig_size = fig_size

    def plot_88(self, index=0):
        img_list = []
        for i in os.listdir(self.big_path):
            img_path = os.listdir(os.path.join(self.big_path, i))[index]
            img_path = os.path.join(self.big_path, i, img_path)
            img_list.append(img_path)

        num_rows = self.num_rows
        num_cols = self.num_cols

        fig, axs = plt.subplots(num_rows, num_cols, figsize=self.fig_size)

        for i, file_path in enumerate(img_list):
            row_idx = i // num_cols
            col_idx = i % num_cols
            axs[row_idx, col_idx].imshow(mpimg.imread(file_path))
            axs[row_idx, col_idx].set_title(str(i))

        plt.show()

    def plot_all_font(self, class_index):
        num_rows, num_cols = self.factor_finder(len(os.listdir(self.big_path)))
        pass

    @staticmethod
    def factor_finder(num):
        factor_list = []
        for i in range(1, num+1):
            if num % i == 0:
                factor_list.append(i)

        middle_factor = len(factor_list) // 2
        return factor_list[middle_factor - 1], factor_list[middle_factor]
