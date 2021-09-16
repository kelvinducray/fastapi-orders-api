import logging
import os
from functools import lru_cache

from psycopg2.extensions import make_dsn
from pydantic import BaseSettings

logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    DEPLOYED_ENVIRONMENT: str = os.getenv("DEPLOYED_ENVIRONMENT", "DEV")

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DSN: str = make_dsn(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
    )


@lru_cache()
def get_settings() -> BaseSettings:
    logger.info("Loading settings...")
    return Settings()
