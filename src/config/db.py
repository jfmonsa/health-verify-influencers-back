"""db configuration."""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from config import env_vars

engine = create_async_engine(env_vars.DB_CONNECTION_STRING, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

