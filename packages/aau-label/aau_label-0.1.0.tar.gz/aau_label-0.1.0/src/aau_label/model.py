from dataclasses import dataclass
from typing import Sequence


@dataclass
class Label:
    x: int
    y: int
    width: int
    height: int
    classifier: str


@dataclass
class LabelImage:
    path: str
    width: int
    height: int
    labels: Sequence[Label]
    source: str | None = None


@dataclass
class COCOLicense:
    name: str
    url: str


@dataclass
class COCOInfo:
    year: int
    version: str
    description: str
    contributor: str
    url: str
    date_created: str
