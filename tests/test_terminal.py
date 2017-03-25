from unittest.mock import Mock

import pytest

from blitsh import terminal
from blitsh.commands import Command, NoOpArguments, ArgParseError


def test_parse_empty_line():
    term = terminal.Terminal(client=Mock())
    assert term.parse_line('') == (None, [])


def test_parse_line_returns_extracts_command_name():
    term = terminal.Terminal(client=Mock())
    assert term.parse_line(':ham spam') == ('ham', [':ham', 'spam'])


def test_empty_command_names_returns_none():
    term = terminal.Terminal(client=Mock())
    assert term.parse_line(': foo') == (None, [])


def test_raises_exception_if_commands_with_same_name_are_registered():
    class Cmd(Command):
        name = 'cmd'

    with pytest.raises(AttributeError) as exc_info:
        terminal.Terminal(client=Mock(), commands=[Cmd(), Cmd()])

    assert str(exc_info.value) == "Some command names are duplicated: cmd"


def test_calls_command():
    class Cmd(Command):
        name = 'ham'

        def parse_args(self, *args):
            return {'first': args[1], 'second': args[2]}

    cmd = Cmd()
    cmd.execute = Mock()
    cmd.execute.return_value = 'return value'
    term = terminal.Terminal(client=Mock(), commands=[cmd])
    term.stdout = Mock()

    assert term.onecmd(':ham spam egg') is False
    cmd.execute.assert_called_once_with(
        term.client, first='spam', second='egg')
    term.stdout.write.assert_called_once_with('return value')


def test_handles_unknown_commands():
    term = terminal.Terminal(client=Mock())
    term.stdout = Mock()

    assert term.onecmd(':ham') is False
    term.stdout.write.assert_called_once_with("unknown command 'ham'\n")


def test_do_not_execute_command_on_no_op():
    class Cmd(Command):
        name = 'ham'

        def parse_args(self, *args):
            raise NoOpArguments("spam")

    cmd = Cmd()
    cmd.execute = Mock()
    term = terminal.Terminal(client=Mock(), commands=[cmd])
    term.stdout = Mock()

    assert term.onecmd(':ham') is False
    assert cmd.execute.called is False
    term.stdout.write.assert_called_once_with('spam\n')


def test_do_not_execute_command_on_parse_error():
    class Cmd(Command):
        name = 'ham'

        def parse_args(self, *args):
            raise ArgParseError("spam")

    cmd = Cmd()
    cmd.execute = Mock()
    term = terminal.Terminal(client=Mock(), commands=[cmd])
    term.stdout = Mock()

    assert term.onecmd(':ham') is False
    assert cmd.execute.called is False
    term.stdout.write.assert_called_once_with('spam\n')
