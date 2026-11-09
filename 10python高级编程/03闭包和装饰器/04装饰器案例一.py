import time


# 装饰器案例一：给多个函数增加一个：输出“函数执行时间”的功能

def time_print(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        wait_time = (end - start) * 1000  # 标示为毫秒
        print(f'{func.__name__} 运行时间为：{wait_time}')

    return inner


@time_print
def test1():
    for i in range(100):
        print(i)
    time.sleep(1.5)  # 暂停1.5秒


# 测试
if __name__ == '__main__':
    test1()
