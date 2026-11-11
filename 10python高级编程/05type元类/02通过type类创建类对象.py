# type为造物者，可以通过type造出类

# 这里定义的Person类在程序执行时，解释器会通过type创建，不多是自动的，我们通过模拟python解释器手动创建一个一模一样的Person感受一下。
class Person:
    # 定义类属性
    age = 10
    pass


# python解释器的执行顺序是自上而下的，一行一行向下走。
p1 = Person  # 类对象赋值给p
print(p1.__class__)  # 看一下p是谁创建的 输出： <class 'type'>
print(p1.age)  # 类对象的属性打印 输出：10

######### [模拟python解释器手动创建一个自定义类]
# className、父类(元组结构)、属性（字典结构）
p2 = type('Person', (object,), {'age': 10})
print(p2.__class__)  # 输出：<class 'type'>
print(p2.age)  # 输出：10

######### [实例化对比：解释器自动与手动]
# 类对象实力化一个对象
p1Object = p1()
p2Object = p2()
# 解释器自动：age:10 type:<class '__main__.Person'> 4350089200
print(f'解释器自动：age:{p1Object.age} type:{type(p1Object)} {id(p1Object)}')
# 模拟解释器手动 ：age:10 type:<class '__main__.Person'> 4350095920
print(f'模拟解释器手动 ：age:{p2Object.age} type:{type(p2Object)} {id(p2Object)}')

print(f'p1 == p2? {p1 == p2}')  # False
print(f'p1Object == p2Object? {p1Object == p2Object}')  # False


######### [总结]
# 了解了type元类后（metaclass）后期我们可以手动的动态话创建类对象，并实力化类对象，然后进行实例化类对象的操作。
# type就是python在背后用来创建类的元类。