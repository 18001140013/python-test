## [1] 线程概念：
# Python中有GIL的概念，它是全局解释器锁，每个线程在执行的时候都要先获取到GIL锁。
# 通过锁实现了： 同一个进程中同一时刻只能有一个线程执行程序，所以在Python中多个线程执行不是【并行】的，而是【并发】的。
import time
from threading import Thread, current_thread, Lock


## [2] 多线程创建
# 方法1: 实例化Thread对象
def test_run():
    sum = 0
    for i in range(100):
        sum = sum + 1
    time.sleep(0.3)
    print(f'{current_thread()}结果：{sum}')


testThread1 = Thread(target=test_run, name='test_T1')
testThread1.start()  # 启动并执行
testThread1.join()


# 方法2: 继承Thread类 实现run方法
class TestThread(Thread):
    def run(self):
        sum = 0
        for i in range(100):
            sum = sum + 1
        time.sleep(0.3)
        print(f'{current_thread()}结果：{sum}')


testThread2 = TestThread(name='test_T2')
testThread2.start()  # 启动并执行
testThread2.join()

## [3] 多线程执行多任务
## [4] 线程不安全的情况
sum_g = 0


def func1_run(x: int):
    global sum_g
    for i in range(x):
        sum_g = sum_g + 1
    print(f'{current_thread()}func1_run={sum_g}')


# 测试例子：总和结果应该是：1500000
count: int = 100 * 10000
func1_T1 = Thread(target=func1_run, args=(int(count / 2),), name='func1_T1')
func1_T2 = Thread(target=func1_run, args=(int(count / 2),), name='func1_T2')
func1_T3 = Thread(target=func1_run, args=(int(count / 2),), name='func1_T3')

# [5] 同步锁 解决并发问题
func1_T1.start()
func1_T1.join()
func1_T2.start()
func1_T2.join()
func1_T3.start()
func1_T3.join()

print(f'{current_thread()}func1_run={sum_g}')

## [6] 互斥锁lock谁抢到谁执行，其他排队等待
sum_g2 = 300 * 10000
lock = Lock()


def func2_run(x: int):
    lock.acquire()  # 竞争锁
    global sum_g2
    for i in range(x):
        sum_g2 = sum_g2 - 1
    print(f'{current_thread()}func2_run={sum_g2}')
    time.sleep(0.3)
    lock.release()  # 释放锁


# 测试例子：sum_g2递减，结果应该=0
func2_T1 = Thread(target=func2_run, args=(int(sum_g2 / 3),), name='func2_T1')
func2_T2 = Thread(target=func2_run, args=(int(sum_g2 / 3),), name='func2_T2')
func2_T3 = Thread(target=func2_run, args=(int(sum_g2 / 3),), name='func2_T3')

# 互斥锁解决并发问题
func2_T1.start()
func2_T2.start()
func2_T3.start()

## [7] 死锁情况
# 用10个线程通过下标去取数组串的值 ，通过lock线程排队，一旦程序崩溃或return返回没有执行到lock.release()释放，
# 则其他等待线程一直排队无法获取到锁，导致正常程序无法执行了就是：死锁情况
# 通过with关键字 自动释放锁，避开死锁情况
lis = ['a', 'b', 'c', 'd', 'e', 'f']
lock2 = Lock()


# 死锁
def func3_error_run(index: int):
    lock2.acquire()
    global lis
    if index >= len(lis):
        print('---- 越界了')
        return
    print(f'{current_thread()}---- {lis[index]}')
    time.sleep(0.3)
    lock2.release()


# 避开死锁
def func3_ok_run(index: int):
    with lock2:
        global lis
        if index >= len(lis):
            print('---- 越界了')
            return
        print(f'{current_thread()}---- {lis[index]}')
        time.sleep(0.3)


for i in range(10):
    Thread(target=func3_ok_run, args=(i,), ).start()


## [8] daemon守护线程
def func5_run():
    while True:
        time.sleep(1)
        print(f'守护线程测试==============={current_thread()}我是死循环')


# daemon=True 表示将主线程作为守护线程，待主线程结束后，子线程自动结束
Thread(target=func5_run, args=(), daemon=True).start()
