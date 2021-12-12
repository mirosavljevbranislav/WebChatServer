from typing import Optional

from starlette.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED

from app.services import user
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi.responses import JSONResponse

SECRET_KEY = "6ad9e80da5855267057ac983fce2ee1ea067b39e6bb478bc61eac514b4c38aa4"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str):
    user_for_auth = user.get_user(username=username)
    if not user_for_auth:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={"Message": "User not found"})
    if not verify_password(password, user_for_auth["password"]):
        return JSONResponse(status_code=HTTP_401_UNAUTHORIZED, content={"Message": "Incorrect username or password"})
    return user_for_auth
