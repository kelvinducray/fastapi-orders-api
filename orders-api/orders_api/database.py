from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import get_settings

settings = get_settings()

POSTGRES_DSN = (
    "postgresql+asyncpg://"
    f"{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}/{settings.POSTGRES_DATABASE}"
)

engine = create_async_engine(
    POSTGRES_DSN,
    echo=True,
)

Session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=True,
    autocommit=False,
    expire_on_commit=False,  # True by default
    info=None,
)

Base = declarative_base()


async def get_db():
    try:
        sess = Session()
        yield sess
    finally:
        await sess.close()
