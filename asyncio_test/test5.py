import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://www.example.com/"
    html = await fetch(url)
    print(html[:100])  # 打印前 100 个字符

asyncio.run(main())
