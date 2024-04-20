from typing import ClassVar, List, Protocol

from PIL.Image import Image

from ..model import Label


class LabelParser(Protocol):
    file_extension: ClassVar[str]

    def parse(self, label_file: str, image: Image) -> List[Label]:
        raise NotImplementedError
