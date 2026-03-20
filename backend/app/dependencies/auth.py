from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/signin")\

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id: str =  payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code = 401, detail = "Invalid token")
        return "User id : " + user_id
    except JWTError:
        raise HTTPException(status_code = 401, detail = "Invalid token")