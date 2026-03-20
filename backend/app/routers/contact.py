from fastapi import APIRouter

from app.schemas import contact

router = APIRouter()

@router.get("/")
async def get_contacts():
    "Get all contacts"
    return {"contacts": []}

@router.post("/")
async def create_contact():
    "Create a new contact"
    return {"message": "Contact created"}
