# 顶级类为object

# 父类
class Person(object):
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

    def eat(self):
        super().eat()  # 调用父
        print('学生可以吃饭')


# 使用
student = Student(name='小丽', age=18, score=100)
student.eat()
student.study()

# object下的dir()方法，可以查看一条线上所有的属性与方法
lis = student.__dir__()
c = 0
for item in lis:
    c += 1
    print(item, end='\n' if c % 5 == 0 else '\t' * 3)

# 判断一个对象是否是这个类的实例
print()
print(isinstance(student, Student))  # true
print(isinstance(student, Person))  # true
print(isinstance(student, object))  # true
print(isinstance(student, str))  # false

# 类是否为一个类的子类
print()
print(issubclass(Student, object))  # true
print(issubclass(Student, Person))  # true
print(issubclass(Person, Student))  # false
