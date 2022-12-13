'''
Websocket server example for short connections
'''

import asyncio
import websockets


async def handle(websocket, path):
    '''
    Handle message from the client

    Args:
        :param:websocket: The websocket connection
        :param:path: The path of the client connection
    '''
    print('Client connects', websocket, path)

    msg = await websocket.recv()
    print(f"< {msg}")

    response = f"Received: {msg}"

    await websocket.send(response)
    print(f"> {response}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host", help="host of the websocket connection", default='localhost')
    parser.add_argument(
        "--port", help="port of the websocket connection", default=9386)
    args = parser.parse_args()

    host = args.host
    port = args.port

    start_server = websockets.serve(handle, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
