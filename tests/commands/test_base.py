import pytest

from blitsh.commands.base import Command


def test_raise_exception_if_no_name():
    class Cmd(Command):
        pass

    with pytest.raises(AttributeError) as exc_info:
        Cmd()

    assert str(exc_info.value) == "name attribute is None for Cmd"


def test_not_implemented_error_on_parse_args():
    class Cmd(Command):
        name = 'testing'

    cmd = Cmd()

    with pytest.raises(NotImplementedError) as exc_info:
        cmd.parse_args('a')

    assert str(exc_info.value) == "class Cmd must implement 'parse_args' method"


def test_not_implemented_error_on_execute():
    class Cmd(Command):
        name = 'testing'

    cmd = Cmd()

    with pytest.raises(NotImplementedError) as exc_info:
        cmd.execute(None, foo=0)

    assert str(exc_info.value) == "class Cmd must implement 'execute' method"
