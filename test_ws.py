import asyncio
from websockets.sync.client import connect
import json

def test():
    with connect("ws://localhost:8000/api/ws/notifications?token=YOUR_TOKEN_HERE") as websocket:
        msg = websocket.recv()
        print(len(msg))
