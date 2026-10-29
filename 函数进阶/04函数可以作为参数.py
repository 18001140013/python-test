# 函数作为参数传递

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def calc(func, num1, num2):
    return func(num1, num2)


# 调用
print(f'{calc(add, 2, 3)}')  # 5
print(f'{calc(sub, 2, 3)}')  # -1
