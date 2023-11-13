from sqlalchemy import Boolean, VARCHAR
from sqlalchemy.orm import mapped_column

from pygtd.models import TimestampedModelBase


class Todo(TimestampedModelBase):
    __tablename__ = "todos"

    title = mapped_column(VARCHAR(255), nullable=False)
    completed = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Todo {self.id}: {self.title}>"
