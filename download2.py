import aiohttp
import asyncio

async def fetch(session,url):
    print("发送请求",url)
    async with session.get(url,verify_ssl=False) as response:
        content=await response.content.read()
        filename=url.split(r"/")[-1]
        with open(filename, mode='wb') as file_obj:
            file_obj.write(content)
async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [r"https://i.tuiimg.net/006/2522/2.jpg",
                    r"https://i.tuiimg.net/006/2522/3.jpg",
                    r"https://i.tuiimg.net/006/2522/4.jpg"]
        tasks=[asyncio.create_task(fetch(session,url)) for url in url_list]
        await asyncio.wait(tasks)

async def a():
    print('Suspending a')
    await asyncio.sleep(3)
    print('Resuming a')
    return 'A'


async def b():
    print('Suspending b')

    await asyncio.sleep(1)
    print('Resuming b')
    return 'B'
if __name__ == '__main__':
    async def ma():
        loop=asyncio.get_event_loop()
        task1=loop.create_task(a())
        task2=loop.create_task(b())
        task1.cancel()
        c=await asyncio.gather(task1,task2,return_exceptions=True)
        print(c)
        # return_value_a, return_value_b = await asyncio.wait([a(), b()],return_when="FIRST_COMPLETED")
        # print(return_value_a)
        # print(type(return_value_a))
        # print(return_value_b)
        # print(type(return_value_b))
    asyncio.run(ma())