##### 类属性定义：多个对象都需要用的属性可以提成 类属性

class Student:
    location = '青岛'  # 类属性

    # 构造函数 创建对象时自动执行该方法
    def __init__(self, name='小华', age=30):
        # 实力化属性：self.
        self.name = name
        self.age = age
        print(f'构造函数')  # 实力对象可以访问到->类级别.属性


# 静态方法调用
print(f'类属性：{Student.location}')
Student.location = '北京'
print(f'类属性：{Student.location}')
student1 = Student(name='小明', age=32)
student2 = Student()
print(f'类属性1：{student1.location}')
print(f'类属性2：{student2.location}')
