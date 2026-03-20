from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, auth, products, search, quotes, contact, cart, orders, favourites, how_it_works
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base


app = FastAPI(
    title = settings.APP_NAME,
    description = "Yelen Import API",
    version = "0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000", "http://localhost:8000"], #frontend url
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
#include routers
app.include_router(users.router, prefix = "/users", tags = ["users"])
app.include_router(auth.router, prefix = "/auth", tags = ["auth"])
app.include_router(products.router, prefix = "/products", tags = ["products"])
app.include_router(search.router, prefix = "/search", tags = ["search"])
app.include_router(quotes.router, prefix = "/quotes", tags = ["quotes"])
app.include_router(contact.router, prefix = "/contact", tags = ["contact"])
app.include_router(cart.router, prefix = "/cart", tags = ["cart"])
app.include_router(orders.router, prefix = "/orders", tags = ["orders"])
app.include_router(favourites.router, prefix = "/favourites", tags = ["favourites"])
app.include_router(how_it_works.router, prefix = "/how-it-works", tags = ["how-it-works"])

@app.get("/")
def root():
    return {"status": "ok", "message": "Yelen Import API is running"}




