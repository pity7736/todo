
from os import system

from abc import ABCMeta, abstractmethod
from typing import List


class Menu(metaclass=ABCMeta):

    name = ''

    def __init__(self):
        self.commands = []
        self._set_options()

    def _set_options(self):
        options = self._get_options()
        self.commands.extend(options)

    @abstractmethod
    def _get_options(self):
        pass

    def run(self):
        self._show()
        option = self._get_option()
        self.commands[option].execute()

    def _show(self):
        system('clear')
        print(self.name)
        print('-' * 50)
        for i, command in enumerate(self.commands):
            print('{}) {}'.format(i, command._title))
        print('-' * 50)

    def _get_option(self):
        while True:
            try:
                option = int(input('Digite opción: '))
            except ValueError:
                print('Ingrese un número')
            else:
                if 0 <= option < len(self.commands):
                    break
                print('Opción inválida')

        return option