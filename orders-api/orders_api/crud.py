from uuid import uuid4

from sqlalchemy.future import select
from sqlalchemy.orm import Session

from . import models, schemas


async def get_customer_by_id(db: Session, user_id: int):
    async with db.begin():
        stmt = select(models.Customers).filter(models.Customers.id == user_id)
        result = await db.execute(stmt)
    return result.fetchone()


async def get_customer_by_email(db: Session, email: str):
    async with db.begin():
        stmt = select(models.Customers).filter(models.Customers.email == email)
        result = await db.execute(stmt)
    return result.fetchone()


async def get_customers(db: Session, limit: int = 100):
    async with db.begin():
        stmt = select(models.Customers).limit(limit)
        result = await db.execute(stmt)
    return result


async def create_customer(db: Session, user: schemas.Customer):
    async with db.begin():
        new_user = models.Customers(**user)
        db.add(new_user)
        await db.commit()
        await db.flush(new_user)
    return new_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
