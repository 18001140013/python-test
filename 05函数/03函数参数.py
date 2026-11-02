# 形参：函数接受数据
# 实参：传入的参数
def test(name: str):  # 3.5 之后 形参参数可以声明类型
    print(name)


def student_info(name: str, age: int):
    print(f'{name},{age}')


# 关键字传参方式：函数调用key-value传参，叫关键字传参
student_info(age=20, name='小明')
# 位置传参方式,必要参数必须在关键字参数前面
student_info('小明', 20)


# / 前面只能位置传参，后面不限
def student_info2(name: str, /, age: int):
    print(f'{name},{age}')


# student_info2(name='小明', age=20) # 报错了
student_info2('小明1', 20)  # ok
student_info2('小明2', age=30)  # ok


# * 后面参数只能用关键字传参，前面不限
def student_info3(name: str, *, age: int):
    print(f'{name},{age}')


# student_info3('小华', 30)  # 报错了
student_info3('小华', age=30)  # ok


# 默认传参,必须放在无值参数后面
def student_info4(age: int, name: str = '小强'):
    print(f'{name},{age}')


student_info4(30, '小华', )  # ok
student_info4(age=40)  # ok


# 可变参数:1个或多个 也可以不传
# 单* 类型会变成元组tuple
def student_info5(*args):
    print(f'{type(args)},{args},{args[0]}')


student_info5('小丽', True, 3.14)


# 双* 类型会变成元组dict
def student_info6(**args):
    print(f'{type(args)},{args},{args['name']}')


# student_info6(name='小女', isBo=True, age=3.14)

# 解包使用：
p = {'name': '小女2', 'isBo': '是', 'age': '3.14'}
student_info6(**p)  # 传参数时需要** 解包

pp = {**p}
print(f'我时解包:{pp}')


def _add(a, b):
    return a + b


# 解包操作
lis = [1, 2]
print(_add(*lis))


# 返回值 2个参数
def _test01(a, b) -> tuple:
    return a + b, a - b


a, b = _test01(3, 2)
print(a, b)
