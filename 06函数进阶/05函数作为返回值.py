# 函数作为返回值

# 外出函数
def outer():
    # 内层函数
    def inner():
        print('我是内部函数')

    return inner


# 调用
result = outer()
result()
