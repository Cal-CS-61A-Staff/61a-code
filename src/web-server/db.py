import os
from contextlib import contextmanager

# noinspection PyUnresolvedReferences
import __main__
from sqlalchemy import create_engine

if __main__.__file__.endswith("app.py"):
    engine = create_engine("mysql://localhost/code")
else:
    engine = create_engine(os.getenv("DATABASE_URL"))


@contextmanager
def connect_db():
    with engine.connect() as conn:

        def db(*args):
            try:
                if isinstance(args[1][0], str):
                    raise TypeError
            except (IndexError, TypeError):
                return conn.execute(*args)
            else:
                for data in args[1]:
                    conn.execute(args[0], data, *args[2:])

        yield db
