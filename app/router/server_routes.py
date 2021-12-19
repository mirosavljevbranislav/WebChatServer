from fastapi import WebSocket, WebSocketDisconnect
from app.router import router
from app.model.connection import ConnectionManager


@router.get("/")
async def get():
    return {"Message": "Hello and welcome to our WebChatApp!"}


manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, client_username: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client {client_username} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client {client_username} has left the chat")
