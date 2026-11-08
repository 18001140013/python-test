# 闭包：嵌套函数就是闭包
# 条件：
#   1 必须是一个嵌套函数：函数包含一个函数，外部函数+内部函数
#   2 内部函数使用到了外部函数的任意一个变量
#   3 内部函数作为外部函数的参数返回

# 例子1 外部函数为一个基本类型，内部函数去修改外部函数value
def say_hello(name):
    def say(msg):
        nonlocal name  # 标示此时的name为外在的
        name = '李四'
        print(f'对：{name} 发送了一条消息：{msg}')

    name = '张三'
    say('明天约会啦')  # 调用后会在内部函数中修改掉外部函数中的 name 变量值
    print(name)
    return say


class Info:
    pass


# 例子2 外部函数为对象，此时内部函数去修改对象.value，不用nonlocal 可生效
def say_hello2(a: Info):
    def say(msg):
        # nonlocal a  # 标示此时的name为外在的
        a.name = '李四'  # 永远变成了李四
        print(f'对：{a.name} 发送了一条消息：{msg}')

    a.name = '张三'
    say('明天约会啦')  # 调用后会在内部函数中修改掉外部函数中的 name 变量值
    print(a.name)
    return say


# 测试
if __name__ == '__main__':
    # 此时返回的say函数就叫闭包
    # say = say_hello('张三')
    # say("明天有时间吗")

    info = Info()
    info.name = '张三'

    # 此时返回的say函数就叫闭包
    say2 = say_hello2(info)
    info.name = '王五'
    say2('明天打篮球去')
