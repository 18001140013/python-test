# 类的继承语法：

# 父类
class Person:
    def eat(self):
        print('人可以吃饭')


# 子类
class Student(Person):
    def study(self):
        print('学生可以学习')


# 使用
student = Student()
student.eat()
student.study()
