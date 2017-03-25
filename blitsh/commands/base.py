"""Base components for building custom commands.
"""

from blitsh.client import Client


__all__ = ['CommandException', 'NoOpArguments', 'ArgParseError', 'Command']


class CommandException(Exception):
    pass


class NoOpArguments(CommandException):
    pass


class ArgParseError(CommandException):
    pass


class Command:
    """Base class for a command.  This class is intended to be subclassed
    to produce new commands.

    A Command class must have a name attribute.
    This is the name of the command when called from the interactive terminal.
    You should obviously make sure that this name is unique.
    A command must implements two different type of action.

    The first one is the :func:`~blitsh.commands.base.Command.parse_args` that should be
    overidden to parse any command line argument.

    The second one is the :func:`~blitsh.commands.base.Command.execute` that process the
    execution of the command according to parsed arguments.

    .. code:: python

        from blitsh.commands import Command, NoOpArguments, ArgParseError

        class MyCommand(Command):
            name = 'my_command'

            def parse_args(self, *args):
                if '--help' in *args:
                    raise NoOpArguments('Takes one argument')
                try:
                    return {'who': args[1]}
                except IndexError:
                    raise ArgParseError("No argument given")

            def execute(self, client, who):
                return 'hello %s' % who

    """
    name = None  # type: str

    def __init__(self):
        if self.name is None:
            raise AttributeError(
                "name attribute is None for {}".format(self.__class__.__name__))

    def parse_args(self, *args: str) -> dict:
        """Parses command lines argument.

        If the parse command is not intented to be executed (for exemple, you
        just want to display some help text), a NoOp exception must be raised.

        If some argument fails to correctly parse, a CommandArgError must be
        raised.

        :params args: arguments from the command line. The first element
            of this list is the name of the command.

        :returns: dict to pass to :func:`~blitsh.commands.base.Command.execute`
            as kwargs.
        """
        raise NotImplementedError(
            "class {} must implement 'parse_args' method".format(
                self.__class__.__name__))

    def execute(self, client: Client, **kwargs: dict) -> str:
        """This method do the hard job.

        It receives as parameter avery thing needed to send the correct
        payload.

        :param client: this :class:`~blitsh.client.Client` can be used to
            communicate with a backdoor
        :param kwargs: specific keywords argument sent to the command.

        :returns: result of the command as intended to be display to end user
        """
        raise NotImplementedError(
            "class {} must implement 'execute' method".format(
                self.__class__.__name__))
