# Process join()函数使用
from multiprocessing import Process
import time


# 吃饭进程
class EatProcess(Process):
    def __init__(self, name):
        super().__init__()  # 注意：这个代码必须要写，负责：从系统申请资源、分配资源、拷贝主进程数据
        self.name = name

    # 任务函数，父Process启动后会调用run方法
    def run(self) -> None:
        for i in range(5):
            print(f'{self.name} 吃饭.....')
            time.sleep(1)  # 休眠1秒


# 工作进程
class WorkProcess(Process):
    def __init__(self, name):
        super().__init__()  # 注意：这个代码必须要写，负责：从系统申请资源、分配资源、拷贝主进程数据
        self.name = name

    # 任务函数，用来执行任务的
    def run(self) -> None:
        for i in range(5):
            print(f'{self.name} 学习.....')
            time.sleep(1)  # 休眠1秒


# 测试代码
if __name__ == '__main__':
    p1 = EatProcess(name='eating进程')
    p2 = WorkProcess(name='working进程')
    p1.start()
    # 进程启动后通过join函数，阻塞主进程，一直等到子进程执行结束后，释放阻塞
    p1.join()
    # 多任务通过join函数实现并行-串行

    p2.start()
    # 主进程会在这里等待所有子进程运行结束后，自动退出。
