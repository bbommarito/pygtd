import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class ModelBase(DeclarativeBase):
    __abstract__ = True


class TimestampedModelBase(ModelBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now(datetime.UTC)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )


from pygtd.models.todo import Todo
