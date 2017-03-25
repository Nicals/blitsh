from blitsh.commands import Command
from blitsh.client import Client


class ExecCommand(Command):
    """This commands sends a shell command to the backdoor.
    """
    name = 'exec'

    def parse_args(self, *args: str) -> dict:
        return {'shell_cmd': ' '.join(args[1:])}

    def execute(self, client: Client, shell_cmd: str) -> str:
        return client.send(shell_cmd)
