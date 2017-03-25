import subprocess

from blitsh import backdoors


def test_generates_valid_php_code():
    bd = backdoors.generate_backdoor()
    proc = subprocess.run(['php', '-l'],
                          input=bd.encode(),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert proc.returncode == 0, proc.stderr.decode()
