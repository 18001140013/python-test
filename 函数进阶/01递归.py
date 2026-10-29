import random


# 递归：函数直接或间接调用自身的一种方法
# 用递归实现一个阶乘，6的阶乘 = 6！=6 * 5 * 4 * 3 * 2 * 1
# for
def f_function(number: int):
    sum = 1
    for i in range(1, number + 1):
        sum *= i
    return sum


# 递归
# 需要两件事情：
#       1、递归体：自己调用自己的代码
#       2、结束条件
def fac(n: int):
    if n <= 1:
        return 1  # 结束条件
    else:
        return n * fac(n - 1)  # 递归体


# 一层一层向下传递，一层一层向上回归
# 执行过程：
'''
        ⬇️fac(6) -> return 6 * fac(5)                 // 6*120=720 ⬆️
            ⬇️fac(5) -> return 5 * fac(4)                 // 5*24=120 ⬆️
                ⬇️fac(4) -> return 4 * fac(3)                 // 4*6=24 ⬆️
                    ⬇️fac(3) -> return 3 * fac(2)                 // 3*2=6 ⬆️
                        ⬇️fac(2) -> return 2 * fac(1)                 // 2*1=2 ⬆️
                            ⬇️fac(1) -> return 1                          // 1  ⬆️
'''

print(f'6! 阶乘：{f_function(6)}')
print(f'6! 阶乘：{fac(6)}')


# 例子：1次连接成功或连接次数超过n上限 结束程序
def on_connection() -> int:
    state = random.randint(0, 1)  # 0|1
    print(f'连接======={state}')
    return state


# 1递归体->返回连接结果bool 2结束条件 n:最大连接次数
def connection(n: int = 5) -> bool:
    if n < 1:
        return False
    else:
        return connection(n - 1) or on_connection() == 1


print(f'连接结果：{connection(n=10)}')
