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
        # img_pos = self.getimage_pos2(bbox)
        img_pos = self.getimage_pos2(bbox)
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

    def getimage_pos(self, index: int, bbox: tuple) -> Tuple[int, int]:
        """
        get image position from index and bbox
        :param index: index of image reference to pythainlp all character function
        :param bbox: bbox of text
        :return: (x, y) where image in that index should be
        """

        # kor kai to hor nog hook
        # 0 to 43
        # Thai Number and special character
        # 74 to 87
        # 46, 48, 56, 57
        thai_main = [i for i in range(0, 47)]
        thai_nums_special = [i for i in range(74, 88)]
        sub_special = [48, 49, 56, 57, 61, 68]
        if index in thai_main or index in thai_nums_special or index in sub_special:
            return (
                (self.canvas_size[0] - bbox[2]) // 2,
                (self.canvas_size[1] - bbox[3]) // 2.5,
            )

        float_major = [range(50, 54)]
        float_special = [47, 62, 63, 71, 72, 73]
        if index in float_major or index in float_special:
            return (
                (self.canvas_size[0] - bbox[2]) // 2,
                (self.canvas_size[1] - bbox[3]) // 2.5,
            )

        diving_character = [54, 55]
        if index in diving_character:
            return (
                (self.canvas_size[0] - bbox[2]) // 2,
                (self.canvas_size[1] - bbox[3]) // 2.5,
            )

        # default center
        # 58 to 60 use default
        return (
            (self.canvas_size[0] - bbox[2]) // 2,
            (self.canvas_size[1] - bbox[3]) // 2,
        )

    def getimage_pos2(self, bbox: tuple) -> Tuple[float, float]:
        """
        return default position for all
        :param bbox: bbox of text
        :return: (x, y) where image in that index should be
        """
        x = (self.canvas_size[0] - bbox[2]) / 2
        y = (self.canvas_size[1] - bbox[3]) / 50

        return x, y
