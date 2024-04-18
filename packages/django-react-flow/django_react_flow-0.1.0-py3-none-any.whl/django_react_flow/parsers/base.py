import abc
from pathlib import Path


class Parser(abc.ABC):

    @abc.abstractmethod
    def parse(self, path: Path) -> dict:
        raise NotImplementedError
