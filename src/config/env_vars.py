"""Module for validating environment variables using Pydantic."""

from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Validate and retrieve environment variables."""

    DB_POSTGRE_CONNECTION_STRING: PostgresDsn = Field()
    PERPLEXITY_API_KEY: str = Field()

    class Config:
        """env file configuration."""

        env_file = ".env"

env_vars = AppSettings()
