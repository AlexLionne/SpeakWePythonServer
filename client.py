import asyncio
import pathlib
import ssl
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ssl_context.load_cert_chain(
        pathlib.Path(__file__).with_name('fullchain.pem'),
        pathlib.Path(__file__).with_name('privkey.pem'))

start_server = websockets.serve(hello, 'localhost', 443, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
