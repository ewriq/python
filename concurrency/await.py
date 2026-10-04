import asyncio

async def work():
    print("Started")

    await asyncio.sleep(10)

    print("Finished")

asyncio.run(work())