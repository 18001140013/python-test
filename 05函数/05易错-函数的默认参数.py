# 函数的默认参数，只会在定义函数的一瞬间创建一次，一直复用这一个列表的内存
def test(a, lst1=[1, 2]):
    if a not in lst1:
        lst1.append(a)
        return lst1


print(f'第一次调用结果是：{test(10)}')  # 1、2、10
print(f'第二次调用结果是：{test(20)}')  # 1、2、10、20
print(f'第三次调用结果是：{test(30, lst1=[60, 70])}')  # 60、70、30
print(f'第四次调用结果是：{test(40)}')  # 1、2、10、20、40


# 函数默认参数 这里是数字类型，属于不可变类型，所有不会记忆
def test2(x=10):
    x += 1
    print(x)


test2()  # 11
test2()  # 11
test2()  # 11

###### 函数默认参数：
# 可变类型：list列表、dict字典、set集合
# 不可变类型：数字、字符串、元组
