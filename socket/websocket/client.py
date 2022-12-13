'''
Websocket client example of short connection
'''

import asyncio
import websockets


async def short_connect(url, msg=''):
    '''
    Send msg to url and close the connection

    Args:
        :param: url: The url of the websocket connection
        :param: msg: The message to be sent, if it is empty, it waits for console input, default is ''
    '''
    async with websockets.connect(url) as websocket:

        if not msg:
            msg = input("Send message to {}\n>> ".format(url))

        await websocket.send(msg)
        print(f"> {msg}")

        response = await websocket.recv()
        print(f"< {response}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path", help="path of the websocket connection", default='')
    parser.add_argument(
        "--message", help="Message to be sent immediately", default='')
    parser.add_argument(
        "--host", help="host of the websocket connection", default='localhost')
    parser.add_argument(
        "--port", help="port of the websocket connection", default=9386)
    args = parser.parse_args()

    host = args.host
    port = args.port
    path = args.path
    msg = args.message

    url = 'ws://{}:{}/{}'.format(host, port, path)
    asyncio.get_event_loop().run_until_complete(short_connect(url, msg))
