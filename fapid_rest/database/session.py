from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlmodel import Session, SQLModel

from fapid_rest import settings
from fapid_rest.user import models

engine = create_engine("sqlite:///foo.db", echo=True)

# engine = create_engine(
#     settings.POSTGRES_URL,
#     echo=settings.DEBUG,
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    # Create tables
    SQLModel.metadata.create_all(engine)


DBsession = Annotated[Session, Depends(get_session)]
