from .command import Command


class GetAllTasksCommand(Command):

    def execute(self) -> None:
        print('getting tasks')
