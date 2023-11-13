import os

from sqlalchemy import event, create_engine, Engine, URL
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

url = URL.create(
    drivername="sqlite",
    database=os.path.join(BASE_DIR, "pygtd.db"),
)

engine = create_engine(url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
