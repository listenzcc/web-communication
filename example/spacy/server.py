
'''
Websocket server example for short connections
'''

import spacy
from spacy import displacy

import asyncio
import websockets

nlp = spacy.load("en_core_web_sm")


async def handle(websocket, path):
    '''
    Handle message from the client

    Args:
        :param:websocket: The websocket connection
        :param:path: The path of the client connection
    '''
    def send(response):
        print(f"> {response[:20]}, {len(response)}")
        return websocket.send(response)

    print('Client connects', websocket, path)

    msg = await websocket.recv()
    print(f"< {msg}")

    # ------------------------------------------------
    text = msg
    doc = nlp(' '.join([e for e in text.split() if e]))
    sentence_spans = list(doc.sents)

    # ------------------------------------------------
    html = displacy.render(sentence_spans, style="ent")
    response = '<Ent>:' + html
    # await websocket.send(response)
    # print(f"> {response[:20]}, {len(response)}")
    await send(response)

    # ------------------------------------------------
    html = displacy.render(sentence_spans, style="dep")
    response = '<Dep>:' + html
    # await websocket.send(response)
    # print(f"> {response[:20]}, {len(response)}")
    await send(response)

    response = '<Final>:'
    await send(response)
    # await websocket.send('<Final>:')
    # print(f'Terminate.')
    return


params = dict(
    host='localhost',
    port=9386
)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host", help="host of the websocket connection", default=params['host'])
    parser.add_argument(
        "--port", help="port of the websocket connection", default=params['port'])
    args = parser.parse_args()

    host = args.host
    port = args.port

    start_server = websockets.serve(handle, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
