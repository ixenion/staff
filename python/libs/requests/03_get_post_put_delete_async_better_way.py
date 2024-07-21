import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://www.example.com/')

    print(r)
    # <Response [200 OK]>
    print(r.json())

asyncio.run(main())
