from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def search_products():
    "Search for a product by name"
    return {"message": "Search product"}
