#### 魔术属性 通过内置的几个属性调用获取到一些信息，叫魔术属性；用途：用来查看关系信息的
class Person:
    pass


class Student(Person):
    ''' 这是一个学生类
    用来测试魔术属性的
    '''

    location = '青岛'

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student('小丽', 30)
student.price = 9.9
student.ll = '北京'
# 保存对象/类的自身属性、自定义属性，以字典形式存储
print(student.__dict__)
print(Student.__dict__)

# 查看对象所属类
print(student.__class__.__name__)  # Student

# 查看对象所属类
print(Student.__name__)  # Student

# 当前类上一级的父类名
print(Student.__bases__)  # Person

# 用来获取类、函数的文档注释的
print(student.__doc__)

# 查看当前类所在的模块名
print(student.__module__)  # __main__
