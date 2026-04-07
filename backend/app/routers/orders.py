from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_orders():
    "Get all orders"
    return {"message": "Orders fetched"}

@router.get("/{id}")
async def get_order(id: str):
    "Get order by id"
    return {"message": "Order fetched"}

@router.post("/")
async def new_order():
    "Place a new order"
    return {"message": "New order placed"} 

@router.patch("/{id}")
async def update_order(order_id: str):
    "update order"
    return {"Order id": order_id}

@router.delete("/{id}")
async def cancel_order(id: str):
    "Cancel an order"
    return {"message": "Order cancelled"}    
    