from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def how_it_works():
    """Get how it works information"""
    return {"message": "How it works endpoint"}
