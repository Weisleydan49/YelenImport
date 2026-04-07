from sqlalchemy import Column, String, Integer, Boolean, Text, Float
from datetime import datetime
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    description = Column(Text)
    price = Column(Float)
    quantity_in_stock = Column(Integer)
    category = Column(String)
    created_at = Column(DateTime, default = datetime.utcnow)