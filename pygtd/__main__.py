import click

from pygtd.db import SessionLocal
from pygtd.models import Todo


@click.group()
def cli():
    pass


@cli.group()
def todo():
    pass


@todo.command()
@click.argument("title")
def add(title):
    with SessionLocal() as session:
        new_todo = Todo()
        new_todo.title = title
        session.add(new_todo)
        session.commit()
        click.echo(f"Todo created with ID {new_todo.id}")


def tui():
    print("Hello from TUI")
