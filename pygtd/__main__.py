import click

from pygtd.commands.todo import todo


@click.group()
def cli():
    pass


cli.add_command(todo)


def tui():
    print("Hello from TUI")
