# 匿名函数：就是没有名字的临时函数， python里用 lambda 关键字定义
# 使用条件：一个函数只有一个返回值，并且只有一句代码，可以使用 lambda关键字
# 格式：lambda 参数列表 : 表达式
# 用途：简化代码的

# 有参例子1:
def add(a, b):
    return a + b


# 匿名函数 = lambda 参数:表达式
# 函数赋值给一个变量
# 使用
fac = lambda a, b: a + b
fac2 = lambda a, b: a if a > b else b

print(add(1, 2))
print(fac(1, 2))


# 无参例子2
def test():
    print("您好我过来打印来了")


# 匿名函数
func = lambda: print("您好我过来打印来了")
funcTest = test

# <class 'function'> , <class 'function'>
print(type(func), type(funcTest))
# <function <lambda> at 0x1037d10c0> , <function test at 0x105e1ceb0>
print(func, funcTest)

test()
func()

test2 = test

print(test is fac)  # False
print(fac is test)  # False

print(test2 is test)  # true
print(test is test2)  # true


# 例子3 作为函数传进去
def calc(func, a, b):
    return func(a, b)


print(calc(lambda a, b: a + b, 1, 2))  # 3

ff = lambda a, b: a + b  # a+b默认为返回值,lambda默认会有返回值，默认为 None,这里是a+b
ff2 = lambda a, b: print('a+b')  # a+b默认为返回值 默认为 None
print(ff(3, 4))
print(ff2(4, 4))

# lambda例子 lis通过元素中age排序中使用
# lis.sort() reverse默认为false，为升序
lis = [
    {'name': 'a', 'age': 10},
    {'name': 'b', 'age': 90},
    {'name': 'c', 'age': 30},
    {'name': 'd', 'age': 80},
    {'name': 'e', 'age': 50},
]
# age 降序排序，默认为升序
lis.sort(key=lambda item: item['age'], reverse=True)  # key:指定排序的依据 reverse：是否逆转

print(f'排序结果：{lis}')
