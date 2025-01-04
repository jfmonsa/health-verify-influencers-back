"""Module data base configuration."""

from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from src.config.env_vars import env_vars

engine = create_engine(env_vars.DB_CONNECTION_STRING, echo=True)


def create_db_and_tables() -> None:
    """Create the database and tables with defined models that inherit from SQLModel."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Get a session from the database engine."""
    with Session(engine) as session:
        yield session
