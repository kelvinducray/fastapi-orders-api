import logging

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    """
    This is used to run this script directly in order to create an ER diagram
    """
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
else:
    from .database import Base

logger = logging.getLogger(__name__)


class Customers(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_no = Column(String)


class Orders(Base):
    __tablename__ = "customer_orders"

    order_id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime)
    customer_id = Column(Integer, unique=True)
    product_id = Column(String)
    is_active = Column(Boolean, default=True)


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, unique=True)
    product_price = Column(String)
    is_active = Column(Boolean, default=True)


if __name__ == "__main__":
    """
    This is used to run this script directly in order to create an ER diagram
    """
    from eralchemy import render_er

    logger.warning("Running this script directly only generates an ER diagram")

    render_er(Base, "ER_Diagram.png")

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")
