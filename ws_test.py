import asyncio
import websockets

async def test():
    try:
        async with websockets.connect("ws://localhost:8000/api/ws/notifications?token=invalid_token") as ws:
            print("Connected")
            msg = await ws.recv()
            print(msg)
    except Exception as e:
        print("Error:", e)

asyncio.run(test())
