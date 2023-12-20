import asyncio
import time

async def process_with_asyncio_sleep(n,m,name):
    start_time = time.time()
    for i in range(n):
        print(f"{name} asyncio sleep {i}...")
        await asyncio.sleep(1)
        print(f"{name} {i} done{time.time()-start_time}...")

    for i in range(m):
        print(f"{name} time sleep {i}...")
        time.sleep(1)
    end_time = time.time()
    print(f'I am{name}')
    print(f"{name} Total time: {end_time - start_time} seconds")

async def hello():
    start_time = time.time()
    await asyncio.gather(
        process_with_asyncio_sleep(2,3,'A'),
        process_with_asyncio_sleep(1,3,'B'),

    )
    end_time = time.time()
    print(f'finally:{end_time - start_time}')

#process_with_sleep(3)
# 获取事件循环
loop = asyncio.get_event_loop()
# 使用事件循环来运行协程
loop.run_until_complete(hello())
# 关闭事件循环
loop.close()