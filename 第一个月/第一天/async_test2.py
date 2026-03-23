import aiohttp
import asyncio

async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()

async def main():
    result = await get_data('https://httpbin.org/get')
    print(result)

if __name__ == '__main__':
    asyncio.run(main())