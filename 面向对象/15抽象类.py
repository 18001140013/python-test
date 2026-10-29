#### 抽象类使用，用途：用来约束子类的

# 从adb模块导入
from abc import ABC, abstractclassmethod


# 抽象类用来约束子类的
class Animal(ABC):

    # 定义抽象方法
    @abstractclassmethod
    def speak(self):
        pass

    # 普通方法
    def eat(self):
        pass


# 子类 必须实现父类的抽象方法，不然会报错
class Dog(Animal):
    def speak(self):
        print('小狗汪汪叫')

    def eat(self):
        print('小狗吃饭')


# 错误案例，不实现抽象方法
class Cat(Animal):

    def eat(self):
        print('小猫吃饭')

    pass


# 方法形成指定类型用：
def animal_speak(animal: Animal):
    animal.speak()


# 方法调用实参指定名用=
animal1 = Dog()
animal1.eat()
animal_speak(animal1)

# 如果不实现父类抽象方法，在程序运行时会报错
# TypeError: Can't instantiate abstract class Cat without an implementation for abstract method 'speak'
# 报错的时机：对象实例化时
animal2 = Cat()  # 这一步报错
animal2.eat()
animal_speak(animal2)
