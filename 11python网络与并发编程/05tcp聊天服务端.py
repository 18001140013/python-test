# TCP连接-聊天-服务端

import socket

# 启动服务
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip+端口
socket_server.bind(('127.0.0.1', 8080))

# accept连接阻塞时，这里等待客户端连接的最大数
socket_server.listen(128)

# 用来接受一个客户端的连接 3次握手 成功后返回收发消息socket2、ip+端口
socket2, addr = socket_server.accept()  # 阻塞函数1

# 进入每个客户的聊天中
while True:
    # 监听接受1kb报文字节，然后转utf8格式
    msg = socket2.recv(1024).decode('utf-8')  # 阻塞函数2
    print(f'====>收到客户端{addr} 消息:{msg}')
    # 收到exit消息关闭连接
    if msg == 'exit':
        socket2.close()  # 4次握手
        break

    # 发送一个消息
    sendMsg = input('服务端>')
    socket2.send(sendMsg.encode('utf-8'))

# 关闭服务端套接字
socket_server.close()
