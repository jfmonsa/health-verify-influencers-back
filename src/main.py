"""Main module for the FastAPI application."""

from fastapi import FastAPI

app = FastAPI(title="API for Health Influencer Admin Panel")


@app.get("/ping")
def read_root() -> dict[str, str]:
    """Health check endpoint."""
    return {"message": "pong"}
