from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.routers import products, quotes, contact, how_it_works
from app.core import config
from app.db.session import engine
from app.models import Base

app = FastAPI(
    title = config.YELENIMPORT,
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
app.include_router(products.router, prefix = "/api/products", tags = ["products"])
app.include_router(quotes.router, prefix = "/api/qoutes", tags = ["qoutes"])
app.include_router(contacts.router, prefix = "/api/contacts", tags = ["contacts"])
app.include_router(how_it_works.router, prefix = "/api/how_it_works", tags = ["how_it_works"])

@app.get("/")
def root():
    return {"status": "ok", "message": "Yelen Import API is running"}




