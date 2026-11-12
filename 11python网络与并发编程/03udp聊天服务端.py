# udp 实现服务端 阻塞函数：recvfrom(), 程序不执行进入等待状态
# 127.0.0.1的ip只能本机内使用，局域网通信需要192ip

import socket  # 导入socket模块

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 9999))  # 绑定ip+端口号 端口号范围：0-2的16次方
print('===>服务端已启动')

while True:
    data, address = server_socket.recvfrom(1024)  # 监听接受消息，包长最大为1024b ,int占用4个字节，1个字节1b, 4个字节4b,1024/4 = 256个字
    print(f'===>客户端 ip:{address[0]} 端口号：{address[1]} 发来消息：{data.decode()}')

    msg = input('===>服务端请输入：')
    server_socket.sendto(msg.encode('utf8'), address)

    if msg == 'quit':
        break

server_socket.close()  # 关闭服务
