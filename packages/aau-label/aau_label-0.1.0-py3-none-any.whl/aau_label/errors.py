from pathlib import Path


class LabelError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ClassFileNotFoundError(LabelError):
    def __init__(self, path: Path | str) -> None:
        super().__init__(f"Could now find {path}")


class PascalParseError(LabelError):
    def __init__(self, path: Path | str) -> None:
        super().__init__(f"Could not parse {path}")
