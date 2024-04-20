from dataclasses import dataclass
from typing import ClassVar, List
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, ParseError

from PIL.Image import Image

from aau_label.errors import PascalParseError

from ..model import Label
from .protocol import LabelParser


@dataclass
class BoundingBox:
    xmin: int
    ymin: int
    xmax: int
    ymax: int


class PascalParser(LabelParser):
    file_extension = ".xml"

    def parse(self, label_file: str, image: Image) -> List[Label]:
        root = ElementTree.parse(label_file).getroot()
        try:
            return [
                self.__parse_object(child) for child in root if child.tag == "object"
            ]
        except ParseError as e:
            raise PascalParseError(label_file) from e

    def __parse_object(self, element: Element) -> Label:
        classifier: str
        bounding_box: BoundingBox

        for child in element:
            if child.tag == "name":
                classifier = child.text or ""
            elif child.tag == "bndbox":
                bounding_box = self.__parse_bounding_box(child)

        return Label(
            bounding_box.xmin,
            bounding_box.ymin,
            bounding_box.xmax - bounding_box.xmin,
            bounding_box.ymax - bounding_box.ymin,
            classifier,
        )

    def __parse_bounding_box(self, element: Element):
        xmin: int
        ymin: int
        xmax: int
        ymax: int

        for child in element:
            if child.tag not in {"xmin", "ymin", "xmax", "ymax"}:
                continue
            if not child.text:
                raise ValueError(f"{child.tag} is missing")

            if child.tag == "xmin":
                xmin = int(child.text)
            elif child.tag == "ymin":
                ymin = int(child.text)
            elif child.tag == "xmax":
                xmax = int(child.text)
            elif child.tag == "ymax":
                ymax = int(child.text)

        return BoundingBox(xmin, ymin, xmax, ymax)
