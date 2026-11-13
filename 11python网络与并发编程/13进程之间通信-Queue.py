# 进程之间通信 队列方式：Queue
import time
from multiprocessing import Process, Queue


# 生产
def product_data(q: Queue):
    for i in range(5):
        q.put(f'录入数据:{i}')
        time.sleep(0.2)
        pass


# 消费
def consume_data(q: Queue, name):
    while True:
        data = q.get()  # 这里的get函数属于 阻塞方式，queue中没有数据时，程序会暂停在这里，直到有数据
        print(f'{name} 读取数据:{data}')
        pass


if __name__ == '__main__':
    queue = Queue(100)  # 限制存放数据的上限，空：无限， get()取出后会自动销毁
    p1 = Process(target=product_data, args=(queue,))
    # 多个消费者会抢着读取数据，谁能拿到依赖机器
    c1 = Process(target=consume_data, args=(queue, 'ls'))
    c2 = Process(target=consume_data, args=(queue, 'zs'))

    p1.start()
    c1.start()
    c2.start()

    p1.join()  # 生产者结束后，将两个消费者也结束,不然消费者get()函数一直阻塞不会关闭
    c1.terminate()
    c2.terminate()  # 主动结束进程

    print("====程序结束！")
