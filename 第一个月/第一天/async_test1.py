import asyncio


async def test():
    print('开始执行')
    await asyncio.sleep(1)
    print('执行完成')

async def main():
    await test()

if __name__ == '__main__':
    asyncio.run(main())