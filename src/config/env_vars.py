"""Module for validating environment variables using Pydantic."""


from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Validate and retrieve environment variables."""

    DB_CONNECTION_STRING: str = Field()
    PERPLEXITY_API_KEY: str = Field()

    class Config:
        """env file configuration."""

        env_file = ".env"


env_vars = AppSettings()
