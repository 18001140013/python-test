# 闭包：嵌套函数就是闭包
# 条件：
#   1 必须是一个嵌套函数：函数包含一个函数，外部函数+内部函数
#   2 内部函数使用到了外部函数的任意一个变量
#   3 内部函数作为外部函数的参数返回

def say_hello(name):
    def say(msg):
        print(f'对：{name} 发送了一条消息：{msg}')

    return say


# 测试
if __name__ == '__main__':
    # 此时返回的say函数就叫闭包
    say = say_hello('张三')
    say("明天有时间吗")
