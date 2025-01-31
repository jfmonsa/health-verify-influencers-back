"""Module data base configuration."""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

# import all models so SQLModel automatically detects them and creates the tables
from src.config.db_models import *  # noqa: F403
from src.config.settings import env_vars

async_engine = create_async_engine(
    url=env_vars.DB_CONNECTION_STRING, echo=True, connect_args={"ssl": "require"}
)


async def init_db() -> None:
    """Create the database and tables with defined models that inherit from SQLModel."""
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
