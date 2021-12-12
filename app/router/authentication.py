from app.model.user import UserSchema

from app.services.user import store_user
from app.services.authentication import authenticate_user

from app.router import router


@router.post("/login")
async def get(data: dict):
    return authenticate_user(data['username'], data['password'])


@router.post("/register")
async def register_user(data: UserSchema):
    store_user(data)
