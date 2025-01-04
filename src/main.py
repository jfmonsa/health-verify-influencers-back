"""Main module for the FastAPI application."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config.db import create_db_and_tables


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage app lifecycle (life span)."""
    # on startup
    create_db_and_tables()
    yield  # app running


app = FastAPI(lifespan=lifespan)


@app.get("/ping")
def read_root() -> dict[str, str]:
    """Health check endpoint."""
    return {"message": "pong"}
