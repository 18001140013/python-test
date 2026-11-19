# 增加gui界面开发三方库 wxpython,这个三方库底层是c++实现的，跨平台的。
import socket
import threading
import time
from threading import Thread, Lock

import wx
from wx import EVT_BUTTON


# 继承wx.Frame 就是一个窗口
class MyServiceFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, id=100, title='阿华的服务器端', pos=wx.DefaultPosition, size=(500, 500))

        # 创建一个面板,绑定到一个窗口上
        panel = wx.Panel(parent=self)

        box = wx.BoxSizer(wx.VERTICAL)

        top_line = wx.BoxSizer(wx.HORIZONTAL)
        start_service_button = wx.Button(panel, label='启动服务')
        save_log_button = wx.Button(panel, label='保存日志到本地')
        stop_service_button = wx.Button(panel, label='关闭服务')
        top_line.Add(start_service_button, proportion=1, flag=wx.EXPAND, border=5)
        top_line.Add(save_log_button, proportion=1, flag=wx.EXPAND, border=5)
        top_line.Add(stop_service_button, proportion=1, flag=wx.EXPAND, border=5)

        self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.text.SetBackgroundColour("#87CEEB")

        box.Add(top_line, flag=wx.EXPAND)
        box.Add(self.text, proportion=1, flag=wx.EXPAND)

        panel.SetBackgroundColour("#eef5ff")
        panel.SetSizer(box)

        # 按钮绑定点击事件
        self.Bind(event=EVT_BUTTON, handler=self.func_start_service_click, source=start_service_button)
        self.Bind(event=EVT_BUTTON, handler=self.func_save_log_click, source=save_log_button)
        self.Bind(event=EVT_BUTTON, handler=self.func_stop_service_click, source=stop_service_button)

        # 服务端socket管理类
        self.my_service_socket = None

    # 启动服务
    def func_start_service_click(self, event):
        self.my_service_socket = MyServiceSocket(self.append_text)

    # 保存日志
    def func_save_log_click(self, event):
        pass

    # 停止服务
    def func_stop_service_click(self, event):
        if self.my_service_socket is not None:
            self.my_service_socket.stop_socket()
            self.my_service_socket = None

    # 界面追加一条消息 把 GUI 更新任务丢进主线程消息队列
    def append_text(self, text):
        wx.CallAfter(self.on_append_text, text)

    # 界面追加一条消息
    def on_append_text(self, text):
        self.text.AppendText(text)
        self.text.SetInsertionPointEnd()  # 自动滚动到末尾


# service_socket
class MyServiceSocket:
    _client: dict = {}

    def __init__(self, set_msg_callback):
        self.server_socket = None
        self.set_msg_callback = set_msg_callback
        self.__start_socket()

    # 单例
    # def __new__(cls, *args, **kwargs):
    #     print('SinglePerson.__new__')
    #     if not hasattr(cls, '_instance'):  # 不存在时创建一次
    #         # 单下划线也是一个私有属性，只能本文件内访问，双下划线只能本类内访问
    #         cls._instance = super().__new__(cls, *args, **kwargs)
    #     return cls._instance

    # 启动服务
    def __start_socket(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind(('127.0.0.1', 7788))
            self.server_socket.listen(5)
            self.set_msg_callback('服务端ServiceSocket已启动成功！\n')

            Thread(target=self.accept_run, daemon=True).start()  # 子线程中连接，防止主线程阻塞

        except OSError as e:
            if e.errno == 48:  # 服务端：端口被占用 [Errno 48] Address already in use
                print('服务端启动时 发现端口被占用 [Errno 48] Address already in use')

    # 停止服务
    def stop_socket(self):
        socket_lis = list(self._client.values())
        print(f'停止服务个数:{len(socket_lis)}')
        for item in socket_lis:
            item.close_session()

        self.server_socket.close()
        self.server_socket = None
        self.set_msg_callback(f'服务端ServiceSocket已退出完成！\n')
        pass

    # 轮询等待客户端的连接
    def accept_run(self):
        while True:

            try:
                session_socket, client_info = self.server_socket.accept()

                # 客户端连接后第一时间会把名字发来，名字作为key使用
                name = session_socket.recv(1024).decode('utf-8')

                if name not in self._client:
                    # 存放到字典队列
                    session_socket_thread = MySessionSocketThread(
                        name, session_socket,
                        client_info,
                        self.set_msg_callback, self.send_all_client,
                        self.close_session_callback)
                    self._client[name] = session_socket_thread
                    session_socket_thread.start()

                    # 并将欢迎消息打印到界面
                    welcome_client_msg = f'欢迎{name}进入聊天 \n时间: {time.strftime('%Y-%m-%d %H:%M:%S')} \n{'-' * 60}\n'
                    self.set_msg_callback(welcome_client_msg)

                    # 通知给所有客户端
                    self.send_all_client(welcome_client_msg)
            except ConnectionAbortedError:  # Errno 53：Software caused connection abort → 软件中止（mac 高频）
                print('服务端server_socket已关闭')
                break

    # 将消息通知给所有客户端
    def send_all_client(self, msg):
        for client_item in self._client.values():
            if client_item.isOnline:
                client_item.session_socket.send(msg.encode('utf-8'))

    # session_close关闭后移除缓存，从字典中移除
    def close_session_callback(self, name):
        print(f'session_close关闭后移除缓存，从字典中移除{name}')
        self._client.pop(name, None)


# session_socket
class MySessionSocketThread(threading.Thread):

    def __init__(self, name, session_socket, client_info, set_msg_callback, send_all_client, close_session_callback):
        super().__init__()  # 必须调用 Thread 的初始化！
        self.isOnline = True
        self.name = name
        self.session_socket = session_socket
        self.client_info = client_info
        self.set_msg_callback = set_msg_callback
        self.send_all_client = send_all_client
        self.close_session_callback = close_session_callback

    def run(self):
        # 监听客户端发来的消息
        while self.isOnline:
            try:
                msg = self.session_socket.recv(1024).decode('utf-8')
                if not msg:  # 等价 data == b'' 客户端发起【FIN】报文，4次握手，关闭。
                    send_msg = f'{self.name}离开了聊天室\n时间: {time.strftime('%Y-%m-%d %H:%M:%S')} \n{'-' * 60}\n'
                    self.set_msg_callback(send_msg)
                    self.send_all_client(send_msg)
                    break

                send_msg = f'{self.name}：{msg}\n时间: {time.strftime('%Y-%m-%d %H:%M:%S')} \n{'-' * 60}\n'
                self.set_msg_callback(send_msg)
                self.send_all_client(send_msg)

            except OSError as e:  # 【本地主线程socket.close后=其他线程还在recv 属于正常报错】
                # Errno9：本地已经close了socket，属于预期内的正常退出
                if e.errno == 9:
                    print(f'服务Session {self.name} 本地主动关闭连接，接收线程退出 \n')
                    break
                else:
                    print(f'服务Session {self.name} 网络异常：{e} \n')
                    break

            except ConnectionResetError:  # 对方 RST 暴力断开
                self.set_msg_callback(f'服务Session {self.name} 异常close \n')
                break

        self.close_session()  # 退出循环 关闭服务

    lock = Lock()

    def close_session(self):
        with self.lock:
            if self.session_socket is not None:
                self.session_socket.close()  # 主动关闭一次
                self.session_socket = None
                self.close_session_callback(self.name)  # 关闭后执行回调


if __name__ == '__main__':
    # wx库中所有的函数都是以大写字母开头
    app = wx.App()  # 创建一个app
    frame = MyServiceFrame()  # 创建一个窗口
    frame.Show()
    app.MainLoop()  # 启动app循环
