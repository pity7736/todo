from .command import Command


class ExitCommand(Command):

    def __init__(self):
        super(ExitCommand, self).__init__(title='Exit')
        self._closed = False

    def execute(self) -> None:
        self._closed = True

    def is_closed(self) -> bool:
        return self._closed
