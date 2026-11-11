# type 是所有对象的创建者
# object 是所有类对象的父类
# 对象分为：（类型）类对象class、非类型对象
# 实例化对象是由 -> 类对象创建出来的 -> 类对象是由type元类对象创建出来的（metaclass）
# 只有类对象才有父对象

# 查看对象是由谁创建：__class__
# 查看对象的父类是谁：__bases__

# 类本身不过是名为type类的一个实例，《对象是谁创建的就是谁的实例》《实例对象没有父子关系，只有类对象有》
# 所以：Person是名为type的一个实例
# type这个类就是造物的上帝，一切类都是由他创造出来的，然后创造出来的类可以再实例化对象，再用实例化对象解决问题。
# 自定义类是怎么创造出来的？python会通过type的 __call__运算符出来的。
class Person:  # 这里是自定义类，定义类后，解释器解释加载后会通过type创建Person类对象，真正发生是：python会通过type的 __call__运算符
    pass


p = Person()  # 实力化对象
num: int = 10


def test():
    pass


func = test

# 由谁创建: type是顶
print(p.__class__)  # 输出：<class '__main__.Person'>
print(Person.__class__)  # 输出：<class 'type'>
print(num.__class__)  # 输出：<class 'int'>
print(int.__class__)  # 输出：<class 'type'>
print(func.__class__)  # 输出：<class 'function'>
print(func.__class__.__class__)  # 输出：<class 'type'>

# 父类是谁： object是顶
print(Person.__bases__)  # 输出：(<class 'object'>,)
print(int.__bases__)  # 输出：(<class 'object'>,)
print(func.__class__.__bases__)  # 输出：(<class 'object'>,)


