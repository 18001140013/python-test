# 定义一个全局变量，测试多个进程是否可以共享这个全局变量
# 不可以：每个进程都是分配独立内存、分配独立cpu资源

import time
from multiprocessing import Process

# 定义一个全局变量，这个全局变量会存放到主进程内存中
lis = ['1']


# lis增加元素 函数1
def test_a():
    for i in range(5):
        lis.append(f'{i}')
        time.sleep(0.3)
    print(f'lis a进程:{lis}')


# lis增加元素 函数2
def test_b():
    for i in range(ord('a'), ord('f')):
        lis.append(chr(i))
        time.sleep(0.3)
    print(f'lis b进程:{lis}')


if __name__ == '__main__':
    p1 = Process(target=test_a, name='a')
    p2 = Process(target=test_b, name='b')

    p1.start()
    p1.join()
    p2.start()
    p2.join()

    lis.append('A')
    lis.append('B')
    print(f'lis 主进程:{lis}')

## 总结：这里总共有三个进程，系统会开辟三个独立内存空间，
#  1、首先主进程空间会建立: lis堆内存、栈中增加名：lis
#  2、然后2个子进程会依次从主内存空间中拷贝lis堆内存数据->到自己的内存空间,栈中增加名字：lis
#  3、验证了进程是：独立的cpu资源、独立的内存空间
