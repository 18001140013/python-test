# property装饰器是一个系统包自带的，增加这个装饰器后，可以让一个函数当成一个属性使用
# 用途场景：私有属性的处理
# 核心作用：简化代码的编写

# 例子
class person:
    # 增加一个私有属性 name
    def __init__(self):
        self.__name = 'lisi'

    @property
    def name(self):
        print("=====get_name=====")
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


# 测试
if __name__ == '__main__':
    person = person()
    print(person.name)
    person.name = 'zhang_san'
    print(person.name)
