import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web,web_runner

def index(request):
    return web.Response(body=b'Awesome',content_type='text/html')

@asyncio.coroutine

def init():
    app = web.Application()
    app = web_runner.AppRunner(app=app).app()
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app._make_handler(),'127.0.0.1',9002)
    logging.info('server started at http://127.0.0.1:9002...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()