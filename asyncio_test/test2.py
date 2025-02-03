import asyncio

async def task(name,dtime):
    print(f"Task {name} start!")
    await asyncio.sleep(dtime)
    print(f"Task {name} finish!")

async def main():
    await asyncio.gather(
        task("A",2),
        task("B",1),
        task("C",3),
    )

async def master():
    task1=asyncio.create_task(task("A",2))
    task2=asyncio.create_task(task("B",1))
    task3=asyncio.create_task(task("C",3))

    await task1
    await task2
    await task3

asyncio.run(master())
