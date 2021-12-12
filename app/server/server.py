from app.router import router as server_router
from app.router.authentication import router as auth_router
from app import app

app.include_router(server_router)
app.include_router(auth_router)
