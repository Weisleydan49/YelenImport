from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_quotes():
    """Get all quotes"""
    return {"quotes": []}

@router.post("/")
async def create_quote():
    """Create a new quote"""
    return {"message": "Quote created"}
