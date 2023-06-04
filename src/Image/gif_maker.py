import os
import imageio
from tqdm.notebook import tqdm
import numpy as np


def gif_generated(folder_path, output_file):
    images = []
    filenames = sorted(os.listdir(folder_path))
    for filename in tqdm(filenames):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            filepath = os.path.join(folder_path, filename)
            image = imageio.v2.imread(filepath)
            inverted_image = np.invert(image)
            images.append(inverted_image)

    imageio.mimsave(output_file, images, duration=0.1)
