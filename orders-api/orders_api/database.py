import asyncio

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base, relationship, selectinload, sessionmaker

from config import get_settings

settings = get_settings()

engine = create_async_engine(
    settings.POSTGRES_DSN,
    echo=True,
)

Base = declarative_base()

Session = sessionmaker(
    bind=None,
    class_=AsyncSession,
    autoflush=True,
    autocommit=False,
    expire_on_commit=False,  # True by default
    info=None,
)


def get_db():
    try:
        sess = Session()
        yield sess
    finally:
        sess.close()
