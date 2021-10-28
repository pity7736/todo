import sys

from .menu import Menu
from todo.commands import ExitCommand


class MainMenu(Menu):

    name = 'Main menu'

    def _get_options(self):
        self._exit_command = ExitCommand()
        commands = (self._exit_command,)
        return commands

    def run(self):
        while self._exit_command.is_closed() is False:
            super(MainMenu, self).run()
        print('Bye')
        sys.exit(0)
