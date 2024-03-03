from pathlib import Path


class Target:
    def __init__(self, *args, **kwargs):
        ...

    def set_property(self, property):
        ...

    def set_language(self, language: str):
        ...

    def set_dialect(self, dialect: int | str):
        ...

    def add_sources(self, *sources: Path):
        ...

class Executable(Target):
    ...

class Library(Target):
    ...
