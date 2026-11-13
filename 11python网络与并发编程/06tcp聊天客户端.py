# TCP连接-聊天-客户端
# 通信条件：ip+端口，端口：0-2的16次方 1024以内的占用的比较多，从之后的取会更好。

import socket

# 启动服务
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3次握手与服务端建立连接
socket_client.connect(('127.0.0.1', 8080))  # 阻塞函数1

# 进入聊天
while True:
    # 发送一个消息
    sendMsg = input('客户端>')
    socket_client.send(sendMsg.encode('utf-8'))
    # 收到exit消息关闭连接
    if sendMsg == 'exit':
        break

    # 监听接受1kb报文字节，然后转utf8格式
    msg = socket_client.recv(1024).decode('utf-8')
    print(f'====>收到服务端消息:{msg}')

# 关闭客户端套接字服务
socket_client.close()
