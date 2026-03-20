from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register():
    "Register a new user"
    return {"message": "User registered succesfully!"}

@router.post("/signin")
async def signin():
    "Sign in an existing user"
    return {"message": "User signed in successfully!"}

@router.post("/signout")
async def signout():
    "Sign out the current user"
    return {"message": "User signed out successfully!"}