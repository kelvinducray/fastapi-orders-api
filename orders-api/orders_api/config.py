import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    DEPLOYED_ENVIRONMENT: str = os.getenv("DEPLOYED_ENVIRONMENT", "DEV")

    POSTGRES_HOST: str = "database"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DATABASE: str = "orders"


@lru_cache()
def get_settings() -> BaseSettings:
    logger.info("Loading settings...")
    return Settings()
