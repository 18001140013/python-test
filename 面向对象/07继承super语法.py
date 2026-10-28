# 类的继承语法：子覆写时 使用super(). 调用
# 对父类方法不满意->重写

# 父类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('人可以吃饭')


# 子类
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)  # 调用父
        self.score = score

    def study(self):
        pass
        print(f'学生可以学习 name{self.name} age{self.age} score{self.score}')

    # 重写
    def eat(self):
        super().eat()  # 调用父
        print('学生可以吃饭')


# 使用
student = Student(name='小丽', age=18, score=100)
student.eat()
student.study()
