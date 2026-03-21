from pydantic import BaseModel, EmailStr

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    message: str
    phone: str

class ContactOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: str
    created_at: str

    class Config:
        from_attributes = True