import asyncio

async def producer(queue):
    for i in range(5):
        print(f"Produce {i}")
        await queue.put(i)
        await asyncio.sleep(1)

async def consumer(queue):
    while True:
        item=await queue.get()
        print(f"Consume {item}")
        queue.task_done()

async def main():
    queue=asyncio.Queue()
    
    producer_task=asyncio.create_task(producer(queue))
    consumer_task=asyncio.create_task(consumer(queue))

    await producer_task
    await queue.join()
    consumer_task.cancel()

asyncio.run(main())




