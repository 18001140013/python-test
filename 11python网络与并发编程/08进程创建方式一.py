# 创建多个进程演示并行效果
# 实例化进程类：Process

import time
from multiprocessing import Process


# 吃饭进程
def eating() -> None:
    for i in range(5):
        print(f' 吃饭.....')
        time.sleep(1)  # 休眠1秒


# 工作进程
def working() -> None:
    for i in range(5):
        print(f' 学习.....')
        time.sleep(1)  # 休眠1秒


# 测试代码
if __name__ == '__main__':
    p1 = Process(target=eating, name='eating进程')
    p2 = Process(target=working, name='working进程')
    p1.start()
    p2.start()
    # 总共有3个进程，主进程会在这里等待这2个子进程都运行结束后，自动退出。
