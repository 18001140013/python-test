# 实现一个单例模式设计，防止一个类多次实例化

# 方式2:在type类下函数实现，相等于在创建类对象时，做了处理，只允许创建一次类对象
class SingleMateClass(type):
    # 解释器扫描到SinglePerson时会执行__new__ 创建类对象
    def __new__(cls, name, bases, attrs):
        print('=======__new__')
        return super().__new__(cls, name, bases, attrs)

    # 解释器扫描到SinglePerson之后会调用这个函数
    def __init__(cls, *args, **kwargs):
        cls._instance = None  # 定义一个标记属性
        print('=======__init__')
        super().__init__(*args, **kwargs)

    # SinglePerson()实例化时会调用__call__这个函数
    def __call__(cls, *args, **kwargs):
        print('=======__call__')
        if cls._instance is None:  # 通过标记实例化对象
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


# 指定元类即可实现单例设计
class SinglePerson(object, metaclass=SingleMateClass):
    age = 100
    pass


# 测试代码
if __name__ == '__main__':
    print('测试代码：', SinglePerson.__mro__)  # 继承关系
    p = SinglePerson()
    p2 = SinglePerson()
    p3 = SinglePerson()
    print(id(p), id(p2), id(p3))
    print(p is p2 is p3)  # is 属于id比较
