from pydantic import BaseModel, Field
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    description: int 
    price: float
    stock: int
    category: str
    image_url: Optional[str] = None
    brand: Optional[str] = None
    colour: Optional[str] = None
    discount: Optional[float] = None


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category: Optional[str] = None
    image_url: Optional[str] = None
    brand: Optional[str] = None
    colour: Optional[str] = None
    discount: Optional[float] = None

class ProductOut(BaseModel):
    name: str
    description: int 
    price: float
    stock: int
    category: str
    image_url: Optional[str] = None
    brand: Optional[str] = None
    colour: Optional[str] = None
    discount: Optional[float] = None
    created_at: datetime
    updated_at: datetime

    class Config():
        form_attributes = True
