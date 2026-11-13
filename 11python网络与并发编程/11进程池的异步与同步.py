# Pool 异步执行与同步执行：apply、apply_async、close、join
from multiprocessing import Pool
import time


# 吃饭任务
def eating(name):
    for i in range(5):
        print(f'{name} 吃饭.....')
        time.sleep(1)  # 休眠1秒


# 工作学习任务
def working():
    for i in range(5):
        print('学习.....')
        time.sleep(1)  # 休眠1秒


# 游戏任务
def game():
    for i in range(5):
        print('游戏.....')
        time.sleep(1)  # 休眠1秒


# 测试代码
if __name__ == '__main__':
    process_pool = Pool(2)  # 定义一个进程池，进程池用来管理与限制进程的上限，都是在内部实现的，如果没有进程池，进程则会由主进程管理。

    ##  apply 属于阻塞函数，同步执行：一个进程执行完了执行下一个进程
    # process_pool.apply(eating, args=('小明',))
    # process_pool.apply(working)

    ##  apply_async 属于非阻塞函数，异步执行 apply:申请
    process_pool.apply_async(eating, args=('小明',))
    process_pool.apply_async(working)

    ## 此时再增加一个任务，进程数不够了，就需要等待空闲进程出来了才会执行此任务
    process_pool.apply_async(game)

    process_pool.close()  # 关闭池子内所有的进程
    ## 异步执行时 还没等子进程运行，主进程就结束了，所以我们要加一个join等待池子所有进程结束后再关闭
    process_pool.join()
