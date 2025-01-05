"""Main module for the FastAPI application."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config.db import init_db


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage app lifecycle (life span)."""
    # on startup
    await init_db()
    # app execution
    yield


app = FastAPI(title="API for Health Influencer Admin Panel", lifespan=lifespan)


@app.get("/ping")
def read_root() -> dict[str, str]:
    """Health check endpoint."""
    return {"message": "pong"}


@app.post("/verify")
async def verify_influencer():
    pass
