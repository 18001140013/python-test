# 因为是脚本语言， 可以给指定对象动态 绑定属性、方法
class Student:
    location = '青岛'  # 类属性

    # 构造函数 创建对象时自动执行该方法
    def __init__(self, name='小华', age=30):
        # 实力化属性：self.
        self.name = name
        self.age = age
        print(f'构造函数')


student1 = Student()
student2 = Student()

# 对象1绑定一个属性
student1.sex = '女'
print(f'性别：{student1.sex}')


def on_eat():
    print('吃饭')


# 对象2绑定一个方法
student2.eat = on_eat
student2.eat()
