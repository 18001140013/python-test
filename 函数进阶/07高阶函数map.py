# 高阶函数：把函数作为参数传入，或者返回值是另外一个函数，这样的函数称为高阶函数，高阶函数是函数式编程的体现
# 一句话：将函数作为参数或返回值
# 用途：减少代码的重复、因此程序比较短，开发速度快

# map函数：对一组数据中的每一个元素，统一执行某种操作（加工），并生成一组新数据。
# 简单理解：对数据中的每一个元素统一加工产出一组新的数据
# 功能是：将列表中的元素作为函数的实参传入到 自定义函数中，然后再返回，总返回值是一个迭代器对象
# 语法定义：map(操作函数，序列)
list1 = [1, 2, 3, 4, 5]


def func(item):
    # return item * 2 # 2倍
    # return item ** 2 # 平方
    print(f'item={item}')
    return item ** 3  # 3次方


result = map(func, list1)  # 返回值为迭代器对象 type: class map,与dict不是一样东西，
print(f'type:{type(result)} , value:{result}l')  # map object at 内存值
resultList = list(result)  # 会在函数内去执行函数加工,谨记：执行加工后，map对象result会将迭代清空，再次遍历会是empty
print(f"resultList={resultList}")  # 转换成list
resultList2 = list(result)
print(f"resultList2={resultList2}")  # 结果是：[]
for item in result:  # 遍历时才会执行处理
    print(f"item:{item}", end='、')

##### 谨记：执行map对象加工后，map对象result将会迭代清空掉变为empty，再次迭代遍历时不会执行
##### 所以 每个元素仅会加工一次，一个元素只会走一次加工函数，加工完成后只保留了新数据
#### list -> 加工 -> new_list ,  列表数据经过加工后产生出新的数据，list与new_list不是统一内存

# 例子2
# 匿名函数作为加工函数，转列表数据时进程加工，完成新数据产出
lis = [5, 6, 7, 8, 9]
new_lis = list(map(lambda x: x ** 2, lis))
print(f"例子2 new_lis={new_lis}")
