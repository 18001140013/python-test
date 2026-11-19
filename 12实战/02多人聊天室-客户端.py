# 增加gui界面开发三方库 wxpython,这个三方库底层是c++实现的，跨平台的。
import threading
from threading import Thread

# 打开一个窗口
import wx, socket, time
from wx import EVT_BUTTON


# 继承wx.Frame 就是一个窗口
class MyClientFrame(wx.Frame):
    _lock = threading.Lock()

    def __init__(self, name):
        super().__init__(parent=None, id=100, title=f'{name}的客户端', pos=wx.DefaultPosition, size=(500, 500))
        self.socket_client = None
        self.__isOnline = False
        self.name = name

        # 创建一个面板,绑定到一个窗口上
        panel = wx.Panel(parent=self)

        box = wx.BoxSizer(wx.VERTICAL)

        # 顶部按钮
        top_line = wx.BoxSizer(wx.HORIZONTAL)
        connect_service_button = wx.Button(panel, label='进入聊天室')
        leave_service_button = wx.Button(panel, label='离开聊天室')
        top_line.Add(connect_service_button, proportion=1, flag=wx.EXPAND, border=5)
        top_line.Add(leave_service_button, proportion=1, flag=wx.EXPAND, border=5)

        # 聊天内容
        self.text_content = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.text_content.SetBackgroundColour("#87CEEB")

        # 发送内容
        self.send_content = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.send_content.SetBackgroundColour("#87CEEB")

        # 底部按钮
        bottom_line = wx.BoxSizer(wx.HORIZONTAL)
        clear_button = wx.Button(panel, label='重置')
        send_button = wx.Button(panel, label='发送')
        bottom_line.Add(clear_button, proportion=1, flag=wx.EXPAND, border=0)
        bottom_line.Add(send_button, proportion=1, flag=wx.EXPAND, border=0)

        box.Add(top_line, flag=wx.EXPAND)
        box.Add(self.text_content, proportion=4, flag=wx.EXPAND)
        box.Add(self.send_content, proportion=3, flag=wx.EXPAND)
        box.Add(bottom_line, flag=wx.EXPAND)

        panel.SetBackgroundColour("#eef5ff")
        panel.SetSizer(box)

        # 按钮绑定点击事件
        self.Bind(event=EVT_BUTTON, handler=self.func_connect_service_click, source=connect_service_button)
        self.Bind(event=EVT_BUTTON, handler=self.func_leave_service_click, source=leave_service_button)
        self.Bind(event=EVT_BUTTON, handler=self.func_send_button_click, source=send_button)
        self.Bind(event=EVT_BUTTON, handler=self.func_clear_button_click, source=clear_button)

    # 连接服务
    def func_connect_service_click(self, event):
        try:
            self.__isOnline = True

            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.socket_client.connect(('127.0.0.1', 7788))  # 阻塞函数1

            # 启动子线程接受服务端消息
            Thread(target=self.recv_run, daemon=True).start()

            # 发送名字
            self.socket_client.send(self.name.encode('utf-8'))

        except ConnectionRefusedError:  # [Errno 61]  表示服务端服务没有启动
            print('表示服务端服务没有启动!')

    # 重置发送内容
    def func_clear_button_click(self, event):
        self.send_content.SetValue('')

    # 退出socket
    def func_leave_service_click(self, event):
        with self._lock:
            if self.__isOnline:
                self.__isOnline = False
                self.socket_client.close()
                self.socket_client = None

    # 发送消息到服务端
    def func_send_button_click(self, event):
        if self.__isOnline:
            msg = self.send_content.GetValue().strip().encode('utf-8')
            self.socket_client.send(msg)
            self.func_reset_button_click(None)

    # 清空全部内容
    def func_reset_button_click(self, event):
        self.send_content.SetValue("")

    # 轮询服务端发来的消息
    def recv_run(self):
        while self.__isOnline:
            try:
                msg = self.socket_client.recv(1024).decode('utf-8')
                if not msg:  # 等价 data == b'' 服务端发起【FIN】报文，4次握手，关闭。
                    self.append_text(f'服务端离开了聊天室\n时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n{'-' * 60}\n')
                    break

                # 并将欢迎消息打印到界面
                welcome_client_msg = f'{msg}'
                self.append_text(welcome_client_msg)

            except OSError as e:  # 【本地主线程socket.close后=其他线程还在recv 属于正常报错】
                # Errno9：本地已经close了socket，属于预期内的正常退出
                if e.errno == 9:
                    print(f'客户端：{self.name} 本地主动关闭连接，接收线程退出 \n')
                    break
                else:
                    print(f'客户端：{self.name} 网络异常：{e} \n')
                    break

            except ConnectionResetError:  # 暴力断开、不握手断开【RST报文】剩下的数据我全部不要了
                print(f'客户端：{self.name} 异常close \n')
                break

        self.func_leave_service_click(None)  # 退出循环 关闭服务

    # 界面追加一条消息 把 GUI 更新任务丢进主线程消息队列
    def append_text(self, text):
        wx.CallAfter(self.on_append_text, text)

    # 界面追加一条消息
    def on_append_text(self, text):
        self.text_content.AppendText(text)
        self.text_content.SetInsertionPointEnd()  # 自动滚动到末尾


if __name__ == '__main__':
    str_name = input('请输入您的姓名：')
    # wx库中所有的函数都是以大写字母开头
    app = wx.App()  # 创建一个app
    frame = MyClientFrame(name=str_name)  # 创建一个窗口
    frame.Show()
    app.MainLoop()  # 启动app循环
