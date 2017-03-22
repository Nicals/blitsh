from pathlib import Path

from click.testing import CliRunner

from blitsh.cli import cli


def test_generate_writes_new_file():
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['generate', 'backdoor.php'])
        assert result.exit_code == 0
        path = Path('backdoor.php')
        assert path.is_file() is True
        assert path.stat().st_size > 0
