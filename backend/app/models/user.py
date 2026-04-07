from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

id = Column(Integer, primary_key = True, index = True)
email = Column(String, unique = True, index = True)
hashed_password = Column(String)
full_name = Column(String)
is_active = Column(Boolean, default = True)
created_at = Column(DateTime, default = datetime.utcnow)

"""Relationships"""

cart = relationship("Cart", back_populates = "user")
orders = relationship("Order", back_populates = "user")
quotes = relationship("Quotes", back_populates = "quotes")
