"""Command line entry point.
"""

import click

from blitsh import backdoors


@click.group()
def cli():
    pass


@cli.command()
@click.argument('path', metavar='PATH', type=click.File('w'))
def generate(path):
    """Generates a new backdoor and save in the PATH file
    """
    path.write(backdoors.generate_backdoor())
