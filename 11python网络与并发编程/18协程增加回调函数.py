# 协程增加回调用：协程结束后将结果传给下一个任务函数
# coroutine.add_one_callback()
import asyncio
import time
from functools import partial


# 定义一个协程回调 有参数
def coroutine_callback(coro, *, time, name, ):  # time与name指定为关键字传参
    print(f'收到参数：{coro.result()},  时间：{time}, 姓名：{name} ')


# 定义一个协程回调 无参数
def coroutine_callback2(coro):
    print(f'收到参数：{type(coro)} {coro.result()} ')  # <class '_asyncio.Task'> work


# 定义一个协程
async def coroutine_work():
    for i in range(3):
        await asyncio.sleep(1)
        print(f'工作：{i}')
    return 'work'


# 定义协程入口
async def coroutine_main():
    c = coroutine_work()
    work_task = asyncio.create_task(c)  # work_task = <class '_asyncio.Task'>
    # work_task.add_done_callback(coroutine_callback2)  # 设置回调:无参调用
    work_task.add_done_callback(partial(coroutine_callback, time=time.time(), name='小花'))  # 设置回调:有参调用
    # await work_task  # 启动:1
    # await asyncio.gather(work_task) # 启动：2
    await asyncio.wait([work_task])  # 启动：3


if __name__ == '__main__':
    print('===开始', time.time())
    asyncio.run(coroutine_main())
    print('===结束')
