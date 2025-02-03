import asyncio

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished")

async def main():
    try:
        await asyncio.wait_for(task("A", 3), timeout=2)
    except asyncio.TimeoutError:
        print("Task A timed out!")

asyncio.run(main())
