## 【1】协程的概念
# 因：多个任务同时执行除了并行就是并发，并发：cpu随机不断切换时间片段执行不同的线程，在python中单个进程只能分配单个cpu,多个线程运行cpu会不断切换。
# 果：cpu不断切换线程，也就是不断切换上下文，切换会占用cpu资源，导致了cpu资源的浪费。
# 避免浪费、充分发挥cpu资源，人为的搞了一套协程，让多个任务的切换放进了单个线程内，单个线程内不断切换多个程序协作的完成任务，就叫协程序。
# 简而言之：用户态下一个线程下的多个子线程，协程。
## 【2】协程的使用姿势
# 导包：asyncio模块下
# async 函数：定义一个协程
# await 函数：挂起一个协程
# asyncio.run(): 启动一个协程入口，内部应该会创建一个线程的

import asyncio, time
from threading import Thread


# 定义一个协程函数
async def func1(name):
    for i in range(6):
        print(f'{name}{i}')
        await asyncio.sleep(1)  # 协程函数：休眠1s，如果不休眠会一直占用线程资源，直到结束
        # time.sleep(1)  # 如果用time下的，会让线程休眠1s,提升了级别


#  【1】定义一个协程入口 【多协程任务串行测试】：
async def main_coroutine():
    await func1('liSi')  # 启动一个协程用await 不然会报错，挂起一个协程就是启动一个协程，等待执行完毕后执行下面
    print(f'main_coro=====liSi 结束')
    await func1('zhangSan')
    print(f'main_coro=====zhangSan 结束')


#  【2】定义一个协程入口 【多协程并行测试 方法1】：
async def main_coroutine_gather():
    print(f'main_coro_gather===== 开始')
    await asyncio.gather(func1('liSi'), func1('zhangSan'))  # 聚集,并发执行多任务，伪并行，需要等待多任务全部执行完
    print(f'main_coro_gather===== 结束')


# 【3】多任务通过多线程执行【多线程并发测试】
def main_thread():
    def funcTest(name):
        for i in range(6):
            print(f'{name}{i}')
            time.sleep(1)  # 线程函数：休眠1s

    t1 = Thread(target=funcTest, args=('liSi',))
    t1.start()
    t2 = Thread(target=funcTest, args=('zhangSan',))
    t2.start()
    t1.join()
    t2.join()


#  【4】定义一个协程入口 【多协程并行测试 方法2】：
async def main_coroutine_create_task():
    print(f'main_coro_create_task===== 开始')
    task1 = asyncio.create_task(func1('liSi'))  # task1类型: # class '_asyncio.Task'，执行到 sleep()方法后会让出时间片
    task2 = asyncio.create_task(func1('zhangSan'))

    # 启动一个异步 方法1
    await task1  # 异步1
    await task2  # 异步2

    # 启动一个异步 方法2
    # await asyncio.gather(task1, task2)

    # 总结 2个异步任务同时执行，一个在sleep时另一个执行 不断切换执行达到并行效果
    print(f'main_coro_create_task===== 结束')


# 测试代码
# await 协程，真正执行
if __name__ == '__main__':
    print(f'=======开始')
    s_time = time.time()

    coro = main_coroutine()  # 查看协程对象类型
    print(f'查看协程对象类型:{type(coro)}')  # class：coroutine
    coro.close()  # 不需要执行就手动关闭

    # asyncio.run(main_coroutine())  # 【1】 启动一个协程串行 12s
    # asyncio.run(main_coroutine_gather())  # 【2】启动一个协程并行 gather方法 6s
    # main_thread()  # 【3】启动一个并发任务-线程 6s
    asyncio.run(main_coroutine_create_task())  # 【4】启动一个异步任务  create_task方法
    print(f'=======结束{time.time() - s_time}')

# 总结：多任务并发，协程执行时间<线程执行时间
