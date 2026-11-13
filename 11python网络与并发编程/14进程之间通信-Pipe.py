# 进程之间通信 管道方式：Pipe
import time
from multiprocessing import Process, Pipe


# 发送
def send_data(p: Pipe):
    for i in range(5):
        p.send(f'录入数据:{i}')
        time.sleep(0.2)
        pass


# 接受
def recv_data(p: Pipe):
    while True:
        data = p.recv()  # 这里的recv函数属于 阻塞方式，pipe中没有数据时，程序会暂停在这里，直到有数据
        print(f'读取数据:{data}')
        pass


if __name__ == '__main__':
    # 创建一个管道 需要2个端点，端点不能多，不然会出错
    send_pi, recv_pi = Pipe()
    sp = Process(target=send_data, args=(send_pi,))
    rp = Process(target=recv_data, args=(recv_pi,))

    sp.start()
    rp.start()

    sp.join()
    rp.terminate()  # 主动结束进程
    print("====程序结束！")
