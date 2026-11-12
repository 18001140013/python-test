# TCP 长连接
# 通信前会进行3次握手，用来保证双方收发正常。 -3次报文
# 关闭通信时需要进行4次挥手，保证双方都能正常退出关闭。-4次报文
## 3次握手过程：
# 1 client  --->      server  SYN=1连接报文、seq=X序列号  // 证明客户端可以发消息
# 2 client  <---      server  ACK=1应答报文、 ack=X+1、 SYN=1、 seq=Y序列号 // 证明服务端可以收发消息
# 3 client  --->      server  ACK=1应答报文、 ack=Y+1 // 证明了客户端可以收到消息
## 4次挥手过程：
# 1 client  --->      server   FIN=1关闭报文、seq=X // 告诉服务端我要关闭 客户端：WAIT1 等待服务端应答，服务端：CLOSE_WAIT
# 2 client  <---      server   ACK=1应答报文、 ack=X+1 // 服务端告诉客户端同意关闭 注意：此时客户端不能再发消息了，但可以接受服务端消息。
# 3 client  <---      server   FIN=1关闭报文、seq=Y、ACK=1、ack=X+1 // 服务端消息发送完毕后发送关闭报文，服务端：LAST_ACK 等待最后一次ACK应答,客户端:WAIT2 注意：此时服务端不能再发消息了。
# 4 client  --->      server   ACK=1 ack=Y+1 // 收到ack后 服务端：CLOSED 关闭，客户端发送ack消息后进入:TIME_WAIT（时间等待） 2*MSL最长报文寿命后自动关闭：CLOSED

## 连接->通信->关闭一个过程：
# 服务端创建Socket_S->绑定bind端口号后进入-> listen，等待客户端的连接，
# 客户端创建Socket_C通过ip+端口连接服务端->connect，服务端收到客户端的连接会进入->accept(同意接受)进行三次握手连接，成功后返回 Socket_S1
# send -> recv
# recv <- send
# Socket_C->CLOSED、Socket_S1->CLOSED
# 服务端等待所有客户端关闭后->Socket_S关闭->CLOSED

# accept三次握手会阻塞，client-a在连接时，listen监听到client-b进来会进行等待阶段。
