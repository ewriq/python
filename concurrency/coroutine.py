import asyncio

async def work():
    print("Working")

coroutine = work()

asyncio.run(coroutine)