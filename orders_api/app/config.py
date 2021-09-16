import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    DEPLOYED_ENVIRONMENT: str = os.getenv("DEPLOYED_ENVIRONMENT", "DEV")


@lru_cache()
def get_settings() -> BaseSettings:
    logger.info("Loading settings...")
    return Settings()
