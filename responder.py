import asyncio
import websockets
import socket

async def send_message(websocket, path):
    ip_address = socket.gethostbyname(socket.gethostname())
    while True:
        message = f"Hello from {ip_address}!"
        await websocket.send(message)
        await asyncio.sleep(5)

start_server = websockets.serve(send_message, "0.0.0.0", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()