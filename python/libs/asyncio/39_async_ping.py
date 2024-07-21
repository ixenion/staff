# aioping
import asyncio
import aioping

async def foo(host:str):
    delay = await aioping.ping(host, timeout=2) * 1000
    print(delay)

host = 'google.com'
host = '10.0.14.4'
asyncio.run(foo(host))
