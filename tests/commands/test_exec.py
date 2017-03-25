from unittest.mock import Mock

from blitsh.commands.exec import ExecCommand


def test_format_args():
    cmd = ExecCommand()

    assert cmd.parse_args(':exec', 'ls', '-lah') == {'shell_cmd': 'ls -lah'}


def test_send_payload():
    client = Mock()
    cmd = ExecCommand()

    assert cmd.execute(client, shell_cmd='ham') is client.send.return_value
    client.send.assert_called_once_with('ham')
