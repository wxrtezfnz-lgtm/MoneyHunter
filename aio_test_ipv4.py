import asyncio
import socket
import aiohttp

async def main():
    connector = aiohttp.TCPConnector(family=socket.AF_INET)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get("https://api.telegram.org") as r:
            print(r.status)

asyncio.run(main())