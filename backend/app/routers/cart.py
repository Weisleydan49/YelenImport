from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.schemas.cart import CartProductCreate, CartProductUpdate

router = APIRouter()

@router.get("/")
async def get_cart(current_user: str = Depends(get_current_user)):
    "Get the user's cart"
    return {"cart": []}

@router.post("/")
async def add_to_cart(product: CartProductCreate, current_user: str = Depends(get_current_user)):
    "Add an item to cart"
    return {"message": "Item succesfully added to cart"}

@router.patch("/{product_id}")
async def update_cart(product: CartProductUpdate, current_user: str = Depends(get_current_user)):
    "Update the quantity of products"
    return {"message": "Quantity updated successfully"}

@router.delete("/{product_id}")
async def remove_from_cart(product_id: str, current_user: str = Depends(get_current_user)):
    "Remove a product from cart"
    return {"message": "product removed from cart"}

@router.delete("/")
async def clear_cart(current_user: str = Depends(get_current_user)):
    "Clear entire cart"
    return {"message": "Cart cleared successfully"}