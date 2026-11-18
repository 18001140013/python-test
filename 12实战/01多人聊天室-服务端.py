# 增加gui界面开发三方库 wxpython,这个三方库底层是c++实现的，跨平台的。
import socket
import threading
import time
from threading import Thread

import wx
from wx import EVT_BUTTON


# 继承wx.Frame 就是一个窗口
class MyServiceFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, id=100, title='阿华的服务器端', pos=wx.DefaultPosition, size=(500, 500))

        # 创建一个面板,绑定到一个窗口上
        panel = wx.Panel(parent=self)

        box = wx.BoxSizer(wx.VERTICAL)

        topLine = wx.BoxSizer(wx.HORIZONTAL)
        start_service_button = wx.Button(panel, label='启动服务')
        save_log_button = wx.Button(panel, label='保存日志到本地')
        stop_service_button = wx.Button(panel, label='关闭服务')
        topLine.Add(start_service_button, proportion=1, flag=wx.EXPAND, border=5)
        topLine.Add(save_log_button, proportion=1, flag=wx.EXPAND, border=5)
        topLine.Add(stop_service_button, proportion=1, flag=wx.EXPAND, border=5)

        self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.text.SetBackgroundColour("#87CEEB")

        box.Add(topLine, flag=wx.EXPAND)
        box.Add(self.text, proportion=1, flag=wx.EXPAND)

        panel.SetBackgroundColour("#eef5ff")
        panel.SetSizer(box)

        # 按钮绑定点击事件
        self.Bind(event=EVT_BUTTON, handler=self.func_start_service_click, source=start_service_button)
        self.Bind(event=EVT_BUTTON, handler=self.func_save_log_click, source=save_log_button)
        self.Bind(event=EVT_BUTTON, handler=self.func_stop_service_click, source=stop_service_button)
        pass

    # 启动服务
    def func_start_service_click(self, event):
        MyServiceSocket(self.text, self.append_text)

    # 保存日志
    def func_save_log_click(self, event):
        pass

    # 停止服务
    def func_stop_service_click(self, event):
        # MyServiceSocket().stop_socket()
        pass

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

    def __init__(self, text: wx.TextCtrl, set_msg_callback):
        self.text = text
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
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', 7788))
        self.server_socket.listen(5)
        self.set_msg_callback('服务端ServiceSocket已启动成功！\n')

        Thread(target=self.accept_run, daemon=True).start()  # 子线程中连接，防止主线程阻塞

    # 停止服务
    def stop_socket(self):
        for item in self._client.values():
            item.close_session()

        self.server_socket.close()
        self.set_msg_callback(f'服务端ServiceSocket已退出完成！\n')
        pass

    # 连接客户端
    def accept_run(self):
        while True:
            if name not in self._client:
                session_socket, client_info = self.server_socket.accept()

                # 客户端连接后第一时间会把名字发来，名字作为key使用
                name = session_socket.recv(1024).decode('utf-8')
                # 并将欢迎消息打印到界面
                welcome_client_msg = f'欢迎{name}进入聊天 \n时间:{time.strftime('%Y-%m-%d %H:%M:%S')} \n{'-' * 60}\n'
                self.set_msg_callback(welcome_client_msg)

                # 存放到字典队列
                session_socket_thread = MySessionSocketThread(
                    name, session_socket,
                    client_info, self.set_msg_callback, )
                self._client[name] = session_socket_thread
                session_socket_thread.start()

            else:
                # 从字典中移除
                self._client.pop(name).close_session()
                self.set_msg_callback('连接已经存在有缓存！')


# session_socket
class MySessionSocketThread(threading.Thread):

    def __init__(self, name, session_socket, client_info, set_msg_callback):
        super().__init__()  # 必须调用 Thread 的初始化！
        self.isOnline = True
        self.name = name
        self.session_socket = session_socket
        self.client_info = client_info
        self.set_msg_callback = set_msg_callback

    def run(self):
        # 监听客户端发来的消息
        while self.isOnline:
            try:
                msg = self.session_socket.recv(1024).decode('utf-8')
                if not msg:  # 等价 data == b''
                    self.set_msg_callback(f'客户端：{self.name} 正常close,连接结束 \n')
                    break

                self.set_msg_callback(f'{msg}\n')
            except ConnectionResetError:  # 对方 RST 暴力断开
                self.set_msg_callback(f'客户端：{self.name} 异常close \n')
                break

    def close_session(self):
        self.session_socket.close()  # 主动关闭一次


if __name__ == '__main__':
    # wx库中所有的函数都是以大写字母开头
    app = wx.App()  # 创建一个app
    frame = MyServiceFrame()  # 创建一个窗口
    frame.Show()
    app.MainLoop()  # 启动app循环
