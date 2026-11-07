# 生成器：也是一种迭代器，也属于可迭代对象，用途：生产与消费
# 定义：函数中定义yield 返回值，关键字 yield, 会将函数变成了一个生成器
# 调用函数时不会立刻执行代码，而是返回了一个生成器
# 通过next()函数会执行一个 yield生成器，然后遇到下一个yield关键次程序会暂停，等待下一次next,如果没有yield关键字，会抛出 StopIteration异常
# next执行->yield暂停->next再执行->yield再暂停....
# send() 函数，就是next()函数功能，不过会给上次暂停的yield 传一次值,并执行一次
# close()函数会中断生成器，中断后再执行next函数时会包 StopIteration异常。

# yield：生产，产生结果

################ 实操代码1 next、send 基本测试 ####################
def generator_func():  # 生产
    value1 = yield yield_func1()
    print(f'====[generator1] {value1}')
    value2 = yield yield_func2()
    print(f'====[generator2] {value2}')
    value3 = yield yield_func3()
    print(f'====[generator3] {value3}')


def yield_func1():
    print('====[yield_func1]')
    return 1


def yield_func2():
    print('====[yield_func2]')
    return 2


def yield_func3():
    print('====[yield_func3]')
    return 3


# 消费
# gf = generator_func()
# print(gf.__next__())  # 1
# print(gf.__next__())  # 2
# print(gf.__next__())  # 3
# print(gf.__next__())  # StopIteration

# 初始化
# gf = generator_func()
# print(f'====[gf] {isinstance(gf, Iterator)}')  # true
# print(f'====[gf] {isinstance(gf, Iterable)}')  # true

# print(gf.__next__()) # 走一次yield
# print(gf.send(100)) #  给上一次yield传一次返回值，再走一次yield ,前提：必须先执行一次next()

# 遍历每一次 yield,直到结束
# for item in gf:
#     result = item
#     print(f'遍历====[result] {result}')

################ 实操代码2 通过close()停止生产器 ####################
def generator_func2(number=0):  # 生产
    while True:
        number += 1
        yield number


gf2 = generator_func2()  # 消费
for item in gf2:
    result = item
    print(f'====[result:] {result}')
    if result >= 50:
        gf2.close()
        break

print('程序执行结束!')


# gf2.__next__() # 最终验证

############## 实操代码3 通过send()停止程序 ######################
def generator_func3(number=0):  # 生产
    while True:
        number += 1
        value = yield number
        # 手动停止条件: 通过send过来的值去判断，send会再取下一次的yield,需要再给一次
        if value == -1:
            yield 0
            break

# gf3 = generator_func3()  # 消费
# for item in gf3:
#     result = item
#     print(f'====[result:] {result}')
#     if result >= 50:
#         print(gf3.send(-1))
#         break
#
# print('程序执行结束!')
# gf3.__next__() # 最终验证
