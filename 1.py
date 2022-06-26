import asyncio
import time

import anyio

async def main():
    print("hello")
    await asyncio.sleep(5)
    print("world")

async def add():
    print("add")
    await asyncio.sleep(10)
    print("func")

if __name__ == '__main__':
    print(time.time())
    tasks=[asyncio.ensure_future(main()),asyncio.ensure_future(add())]
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time())