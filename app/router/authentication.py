from datetime import timedelta

from fastapi import HTTPException
from starlette import status

from app.model.user import UserSchema

from app.services.user import store_user
from app.services.authentication import authenticate_user, create_access_token

from app.router import router

ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post("/login")
async def login_user(data: dict):
    user = authenticate_user(data['username'], data['password'])
    if not user:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['username']}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register")
async def register_user(data: UserSchema):
    if store_user(data):
        return "True"
    else:
        return "False"
