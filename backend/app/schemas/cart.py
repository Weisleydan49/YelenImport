from pydantic import BaseModel, Field
from datetime import datetime

class CartProductCreate(BaseModel):
    product_id: str
    quantity: int

class CartProductUpdate(BaseModel):
    quantity: int

class CartProductOut(BaseModel):
    id: int
    product_id: str
    quantity: int
    added_at: datetime

    class Config:
        from_attributes = True