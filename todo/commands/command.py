from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    def __init__(self, title: str):
        self._title = title

    @property
    def title(self) -> str:
        return self._title

    @abstractmethod
    def execute(self) -> None:
        pass
