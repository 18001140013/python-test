## 协程的返回值与终止
import asyncio


# 定义一个吃饭协程
async def eat_coroutine(name):
    for i in range(6):
        print(f'{name} 吃饭了{i}次')
        await asyncio.sleep(0.5)
    return 'eat'


# 定义一个工作协程
async def work_coroutine(name):
    for i in range(6):
        print(f'{name} 工作了{i}次')
    return 'work'


# 定义一个报错协程
async def error_coroutine():
    raise ValueError('error 执行出错了！！')


# 定义一个协程主入口
async def main_coroutine():
    # 【1】同步执行
    # await eat_coroutine('liSi')
    # await eat_coroutine('zhangSan')
    # await work_coroutine('liSi')
    # await work_coroutine('zhangSan')

    # 【2】异步执行 多任务切换执行谁阻塞了就把资源让出来 方法1:
    # await asyncio.gather(eat_coroutine('liSi'), eat_coroutine('zhangSan')
    #                      , work_coroutine('liSi'), work_coroutine('zhangSan'))

    # 创建异步任务task，默认会启动协程，阻塞时停止
    task1 = asyncio.create_task(eat_coroutine('liSi'), )
    task2 = asyncio.create_task(eat_coroutine('zhangSan'))
    task3 = asyncio.create_task(work_coroutine('小华'))
    # task4 = asyncio.create_task(error_coroutine())

    # 【3】异步执行 方法2:
    # await task1
    # await task2

    # 【4】异步执行 方法3:
    # await asyncio.gather(task1, task2)

    # 【5】异步执行 终止任务、返回结果:
    # task1.cancel()  # 取消后再执行任务 会报错CancelledError , return_exceptions = true关闭了错误
    # result = await asyncio.gather(task1, task2, return_exceptions=True)
    # print(result)  # [CancelledError(''), 'eat']

    # 【6】异步执行 终止任务、返回结果:
    # task1.cancel()  # 取消后再执行任务 会报错CancelledError , return_exceptions = true关闭了错误
    # result：二元元组，done为已完成任务列表，pending还没有完成的任务里诶宝
    # 【return_when】：
    #           1、FIRST_COMPLETED 第一个完成就返回
    #           2、FIRST_EXCEPTION 第一异常就返回
    #           3、ALL_COMPLETED：默认也是全部完成
    # done, pending = result = await asyncio.wait([task3, task2, task1, task4], return_when=asyncio.ALL_COMPLETED)
    done, pending = result = await asyncio.wait([task3, task2, task1], return_when=asyncio.FIRST_COMPLETED)

    for t in done:
        # 异常处理
        if t.exception() is not None:
            print("done任务失败：", t.exception())
        else:
            print("done任务完成：", t.result())

    for t in pending:
        print("pending任务取消：", t.cancel())


if __name__ == '__main__':
    asyncio.run(main_coroutine())  # 启动一个协程

##### 对比：
#       asyncio.wait	            asyncio.gather
# 返回：	(done 集合，pending 集合)	    结果列表
# 顺序：	不保证	                    和入参顺序一致
# 异常：	自己捕获 task.result ()	    return_exceptions 控制

# 1、需要每个任务结果用gather，并return_exceptions=true控制异常
# 2、多个任务不需要结果，但是需要手动取消，选用wait，可以拿到task集合
