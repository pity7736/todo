from .command import Command


class CreateTaskCommand(Command):

    def execute(self) -> None:
        print('creating task')
