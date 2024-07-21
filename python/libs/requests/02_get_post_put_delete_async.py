# 1. Асинхронный GET запрос:

import aiohttp
import asyncio

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.example.com/items') as response:
            data = await response.json()
            return data

async def main():
    data = await fetch_data()
    print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


# 2. Асинхронный POST запрос:

import aiohttp
import asyncio

async def send_data():
    data = {"key": "value"}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.example.com/items', json=data) as response:
            data = await response.json()
            return data

async def main():
    data = await send_data()
    print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


# Аналогично, вы можете использовать функции put и delete для отправки
# PUT и DELETE запросов в асинхронном режиме с помощью aiohttp.
