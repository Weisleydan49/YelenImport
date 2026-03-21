from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_products():
    """Get all products"""
    return {"products": []}

@router.get("/{product_id}")
async def get_product(product_id: str):
    """Get a specific product"""
    return {"product_id": product_id}
