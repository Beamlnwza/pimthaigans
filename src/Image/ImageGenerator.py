import os
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont


class ImageGenerator:
    BLACK: tuple = (0, 0, 0)
    WHITE: tuple = (255, 255, 255)

    def __init__(
            self,
            font_path: str,
            font_size: int = 64,
            canvas_size: Tuple[int, int] = (500, 500),
            font_color: Tuple[int, int, int] = BLACK,
            background_color: Tuple[int, int, int] = WHITE,
    ) -> None:
        """
        Image Generator is a class that generate image from text
        first init with font_path, font_size, canvas_size, font_color, background_color
        for Image constructor

        :param font_path: must end with .ttf
        :param font_size:
        :param canvas_size:
        :param font_color:
        :param background_color:
        """
        self.font_path = font_path
        self.font_size = font_size
        self.canvas_size = canvas_size
        self.font_color = font_color
        self.background_color = background_color

    def generate(self, text: str, out_path: str, index: int, verbose: int = 0) -> None:
        """
        generate image from text and save to out_path with constant style
        include font_path, font_size, canvas_size, font_color, background_color

        :param text: text to generate
        :param out_path: path to save
        :param index: index of image use to find output path
        :param verbose: verbose 1 to print every index, text
        :return:
        """
        if verbose == 1:
            print(f"generate {index} {text}")

        img = Image.new("RGB", self.canvas_size, self.background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font_path, self.font_size)
        bbox = font.getbbox(text)
        img_pos = self.getimage_pos(index=index, bbox=bbox)
        draw.text(img_pos, text, self.font_color, font=font)
        label_out_path = os.path.join(out_path, str(index).zfill(2))
        pic_name = self.check_index(label_out_path)
        pic_name = os.path.join(out_path, str(index).zfill(2), pic_name + ".png")
        img.save(pic_name)

    @staticmethod
    def check_index(output) -> str:
        """
        get what's last number in output folder
        :param output:
        :return: string of last index
        """
        img_in = len(os.listdir(output))
        last_index = str(img_in).zfill(5)

        return str(last_index).zfill(5)

    def getimage_pos(self, index, bbox) -> Tuple[int, int]:

        # default center
        return (
            (self.canvas_size[0] - bbox[2]) // 2,
            (self.canvas_size[1] - bbox[3]) // 2,
        )
