from pydantic.v1 import PathNotExistsError
import email
from app.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

class Contact(Base):
    __tablename__ = "contact"

    contact_id = Column(String, primary_key = True, default = lambda: str(uuid4()))
    name = Column(String, "user.user_name")
    email = Column(String)
    phone = Column(Integer)
    message = Column(String)
    created_at = Column(DateTime, server_default = func.now())