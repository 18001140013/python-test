# udp 实现客户端

import socket  # 导入socket模块

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('===>客户端请输入：')
    client_socket.sendto(msg.encode('utf8'), ('127.0.0.1', 9999))
    data, address = client_socket.recvfrom(1024)  # 监听接受消息，包长最大为1024b ,int占用4个字节，1个字节1b, 4个字节4b,1024/4 = 256个字
    print(f'===>服务端 ip:{address[0]} 端口号：{address[1]} 发来消息：{data.decode()}')

    if data.decode() == 'quit':
        break

client_socket.close()  # 关闭服务
