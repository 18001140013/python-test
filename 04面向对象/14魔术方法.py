#### 魔术方法 用途：用来重写的，跟踪与分析用的
## init 对象初始化
## del 对象销毁
## str 对象输出
## eq 对象比较

class Person:
    pass


class Student(Person):
    # 对象初始化被调用
    def __init__(self):
        print('init')
        pass

    # 对象销毁前被调用
    def __del__(self):
        print('del')
        pass

    # 对象a == 对象b , value:指对象b
    def __eq__(self, value: object, /) -> bool:
        return isinstance(value, Student)  # value 是否为Student的实力
        # return id(self) == id(value)

    def __str__(self) -> str:
        return '对象打印输出'


student = Student()
print(student)
print(f'eq1: {student == 'student'}')
print(f'eq2: {student == Student()}')  # 重写eq 结果：True
