import sys
from typing import Tuple

from .menu import Menu
from todo.commands import ExitCommand, CreateTaskCommand, GetAllTasksCommand, \
    Command


class MainMenu(Menu):

    _name = 'Main menu'

    def _get_options(self) -> Tuple[Command, ...]:
        self._exit_command = ExitCommand()
        commands = (
            CreateTaskCommand('Create task'),
            GetAllTasksCommand('Get all tasks'),
            self._exit_command,
        )
        return commands

    def run(self) -> None:
        while self._exit_command.is_closed() is False:
            super(MainMenu, self).run()
        print('Bye')
        sys.exit(0)
