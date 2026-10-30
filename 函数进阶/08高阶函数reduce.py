# 高阶函数：reduce
from functools import reduce

# reduce函数：对一组数据中 a=上下两个元素的结果、b=下一元素，进行计算，然后返回最终的一个结果
# 简单理解：对数据中的每一个元素相加、相乘，计算出一个最终值
# 功能是：叠加、阶乘等，
# 语法定义：map(function(a,b)，序列, 初始值) -> 返回为一个值 = 叠加结果
list1 = [1, 2, 3, 4, 5]


# 加工函数
def func(a, b):
    print(f'a={a}, b={b}')
    return a + b


# reduce 原貌实现
initial = 0  # 初始值
result = initial  # 初始结果值
for item in list1:
    result = func(result, item)
print(f'==========result1:{result} ')

# reduce 使用
result2 = reduce(func, list1, initial)
print(f'==========result2:{result2}')

# reduce 使用-匿名函数简写
result3 = reduce(lambda a, b: a + b, list1, initial)
print(f'==========result3:{result3}')
