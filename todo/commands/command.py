from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    def __init__(self, title):
        self._title = title

    @property
    def title(self):
        return self._title

    @abstractmethod
    def execute(self):
        pass
