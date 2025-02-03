import asyncio

async def sayhello():
    print("Hello!")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(sayhello())
