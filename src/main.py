"""Main module for the FastAPI application."""
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def read_root() -> str:
    """Health check endpoint."""
    return "pong"
