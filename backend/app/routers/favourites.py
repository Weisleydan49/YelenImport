from fastapi import APIRouter

router = APIRouter()

@router.post("/add")
async def add_to_favourites():
    "Add a product to user's favourites"
    return {"message": "Product added to favourites successfully!"}
