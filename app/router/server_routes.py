from fastapi import WebSocket
from app.router import router


@router.get("/")
async def get():
    return {"Message": "Hello and welcome to our WebChatApp!"}


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
