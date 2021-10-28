from abc import ABCMeta, abstractmethod
from typing import List, Sequence

from todo.commands import Command


class Menu(metaclass=ABCMeta):

    _name = ''

    def __init__(self):
        self._commands: List[Command] = list(self._get_options())

    @abstractmethod
    def _get_options(self) -> Sequence[Command, ...]:
        pass

    def run(self) -> None:
        self._show()
        option = self._get_option()
        self._commands[option].execute()

    def _show(self):
        print('\n\n\n')
        print(self._name)
        print('-' * 50)
        for i, command in enumerate(self._commands):
            print('{}) {}'.format(i, command.title))
        print('-' * 50)

    def _get_option(self) -> int:
        while True:
            try:
                option = int(input('Enter option: '))
            except ValueError:
                print('Option must to be a integer')
            else:
                if 0 <= option < len(self._commands):
                    break
                print('Invalid option')
        return option
