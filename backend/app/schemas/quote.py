from pydantic import BaseModel
from datetme import datetime
from enum import Enum

#client requests
class QuoteCreate(BaseModel):
    product_id: str
    quantity: int
    message: Optional[str] = None

#admin aupdates
class QuoteUpdate(BaseModel):
    status: Optional[str] = None # pending, approve, rejected
    price: Optional[float] = None


class QouteStatus(BaseModel):
    pendind = "pending"
    approved = "approved"
    rejected = "rejected"
 

#What gets returned
class QouteOut(BaseModel):
    id: str
    user_id: str
    product_id: str
    quantity: int
    status: Optional[QuoteStatus] = None
    message: Optional[str] = None
    price: Optional[float] = None
    created_at: datetime


class Config():
    form_attributes = True

