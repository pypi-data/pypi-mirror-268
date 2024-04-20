from __future__ import annotations

import os
from typing import List, Optional

from PIL.Image import Image

from ..errors import ClassFileNotFoundError
from ..model import Label
from .protocol import LabelParser


class DarknetParser(LabelParser):
    file_extension = ".txt"

    def __init__(self):
        self.current_directory: Optional[str] = None
        self.label_map: List[str] = []

    def __parse_row(self, row: str, img_width, img_height) -> Label:
        class_index, x, y, width, height = row.split()

        class_index = int(class_index)
        width = round(float(width) * img_width)
        height = round(float(height) * img_height)
        x = round(float(x) * img_width - width / 2)
        y = round(float(y) * img_height - height / 2)

        return Label(x, y, width, height, self.label_map[class_index])

    def parse(self, label_file: str, image: Image) -> List[Label]:
        self.__load_class_file(label_file)

        with open(label_file, "r") as file:
            width, height = image.size

            try:
                return [self.__parse_row(row, width, height) for row in file]
            except ValueError:
                raise ValueError(f"Badly formatted label file: {label_file}")

    def __load_class_file(self, label_file: str):
        filepath, _ = os.path.split(label_file)

        if self.current_directory == filepath:
            return

        self.current_directory = filepath
        classfile = os.path.join(filepath, "classes.txt")

        try:
            with open(classfile, "r") as file:
                self.label_map = [row.strip() for row in file if row]
        except FileNotFoundError as e:
            raise ClassFileNotFoundError(filepath) from e
