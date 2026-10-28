##### 类方法使用：不需要操作对象数据时，定义类方法 类名.method()
##### 实例方法使用：需要用到对象数据时，定义实例方法 obj.method()
##### 静态方法使用：不需要类、实例数据时，定义静态方法，类名.method() 更像是一个独立的工具函数
class Student:
    location = '青岛'  # 类属性

    # 构造函数 创建对象时自动执行该方法
    def __init__(self, name='小华', age=30):
        # 实力化属性：self.
        self.name = name
        self.age = age
        print(f'构造函数')  # 实力对象可以访问到->类级别.属性

    # 实例方法
    def show_obj_method(self):
        print(f"我是实例方法 {self.age}")

    # 类方法
    @classmethod
    def show_clas_method(cls):
        print(f"我是类方法 {cls.location}")

    # 静态方法
    @staticmethod
    def show_static_method(age):
        if age >= 18:
            print(f"我是静态方法：{age} 成年了")
        else:
            print(f"我是静态方法：{age} 未成年了")


Student.show_clas_method()
Student.show_static_method(age=18)

student = Student()
student.show_obj_method()
