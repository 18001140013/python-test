##### 类的组成部分、怎么定义
class Student:
    location = '青岛'  # 类属性

    # 构造函数 创建对象时自动执行该方法
    def __init__(self, name, age):
        # 实力化属性：self.
        self.name = name
        self.age = age
        print(f'构造函数-对象访问到类级别.属性： {self.location}')  # 实力对象可以访问到->类级别.属性
        self.show_cls_method()  # 实力对象可以访问到->类级别.方法
        self.show_static_method()  # 实力对象可以访问到->静态级别

    # 实力方法
    def show_value(self):
        print(f'这个是实力方法1： {self.name}、{self.age}')

    #     类方法
    @classmethod
    def show_cls_method(cls):  # 类级别可以访问到->静态级别 不能范围到对象级别
        print(f'这个是类方法1： 用@classmethod修饰 location:{cls.location},{Student.location}')

    # 静态方法1
    @staticmethod
    def show_all():  # 静态可以访问到->本类所有级别
        print(f'这个是静态方法1：用@staticmethod修改 {student.age} {Student.location}')

    # 静态方法2
    @staticmethod
    def show_static_method():
        print(f'这个是静态方法2：用@staticmethod修改 {Student.location}')

# 静态方法调用
Student.show_static_method()

# 实力化一个类
student = Student(name='小明', age=30)
print(f"{ {id(student)} }")
print(f"{type(student)}")
print(f"{student}")

# print(f'对象属性：{student.name},{student.age}')
# student.show_value()
# student.show_cls_method()
