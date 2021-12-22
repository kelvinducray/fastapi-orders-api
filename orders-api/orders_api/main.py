import logging

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db
from .models import Base

logger = logging.getLogger("uvicorn")
app = FastAPI()


@app.on_event("startup")
async def startup():
    # Initialise database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Hello World!!!!!"}


@app.get("/test")
async def root(db: Session = Depends(get_db)):
    async with db.begin():
        stmt = select(models.Customers)
        result = await db.execute(stmt)
    logger.info(result)
    return {"message": "Hello World!!!!!"}


@app.post("/users/", response_model=schemas.Customer)
async def create_customer(user: schemas.Customer, db: Session = Depends(get_db)):
    logger.info('************')
    logger.info(user)
    logger.info('###')
    logger.info(models.Customers(**user))
    logger.info('************')
    db_user = await crud.get_customer_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_customer(db=db, user=user)


@app.get("/users/list_all")  # , response_model=schemas.Customer)
async def get_customers(db: Session = Depends(get_db)):
    users = await crud.get_customers(db)
    if not users:
        raise HTTPException(status_code=400, detail="No registered customers")
    return {"message": str([u for u in users])}


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
