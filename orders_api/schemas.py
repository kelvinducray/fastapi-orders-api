from pydantic import UUID4, BaseModel, EmailStr

# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


class Customer(BaseModel):  # Base(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

    # class CustomerCreate(CustomerBase):
    #     pass

    # class Customer(CustomerBase):
    #     id: UUID4

    class Config:
        orm_mode = True
