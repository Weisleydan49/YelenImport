from app.db.ase import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
import uuid

class Cart(Base):
    __tablename__ = "cart_items"

    cart_id = Column(String, primary_key = True, default = lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.user_id"))
    product_id = Column(String, product.product_id)
    quantity = Column (String, nullable = false)
    added_at = Column(DateTime, server_default = func.now())

