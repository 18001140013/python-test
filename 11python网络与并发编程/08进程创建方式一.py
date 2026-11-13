# 创建多个进程演示并行效果
# 实例化进程类：Process

from multiprocessing import Process
import time


# 吃饭任务
def eating():
    for i in range(5):
        print('吃饭.....')
        time.sleep(1)  # 休眠1秒


# 工作学习任务
def working():
    for i in range(5):
        print('学习.....')
        time.sleep(1)  # 休眠1秒


# 测试代码
if __name__ == '__main__':
    p1 = Process(target=eating, name='eating进程')
    p2 = Process(target=working, name='working进程')
    p1.start()
    p2.start()
    # 总共有3个进程，主进程会在这里等待这2个子进程都运行结束后，自动退出。
