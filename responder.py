import asyncio
import socket
from aiohttp import web

async def index(request):
    return web.FileResponse('./index.html')

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    ip_address = socket.gethostbyname(socket.gethostname())
    responder_number = request.match_info['responder']
    
    try:
        while True:
            message = f"Hello from Responder {responder_number} ({ip_address})!"
            await ws.send_str(message)
            await asyncio.sleep(5)
    finally:
        await ws.close()
    return ws

async def main():
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_get('/ws/{responder}', websocket_handler)
    return app

if __name__ == '__main__':
    web.run_app(main(), host='0.0.0.0', port=8000)