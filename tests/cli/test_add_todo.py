import pytest
from click.testing import CliRunner
from sqlalchemy import create_engine

from pygtd.__main__ import cli
from pygtd.db import SessionLocal
from pygtd.models import Todo, ModelBase


@pytest.fixture()
def session():
    engine = create_engine("sqlite://")
    ModelBase.metadata.create_all(engine)
    SessionLocal.configure(bind=engine)
    yield SessionLocal
    ModelBase.metadata.drop_all(engine)


class TestAddTodo:
    def test_it_adds_a_todo(self, session):
        runner = CliRunner()
        # noinspection PyTypeChecker
        result = runner.invoke(cli, ["todo", "add", "Buy milk"])
        assert result.exit_code == 0
        with session() as session:
            assert session.query(Todo).count() == 1
            assert session.query(Todo).first().title == "Buy milk"

    def test_it_echos_a_success_message(self, session):
        runner = CliRunner()
        result = runner.invoke(cli, ["todo", "add", "Buy milk"])

        with session() as session:
            todo = session.query(Todo).first()
            assert result.exit_code == 0
            assert result.output == f"Todo created with ID {todo.id}\n"
