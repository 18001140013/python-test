# 实现一个单例模式设计，防止一个类多次实例化

# 方式1: 在object类函数实现，相等于在SinglePerson()实例化时做了处理
# 通过动态添加私有属性作标记，在函数__new__ 类实例化函数中判断标记而执行1次实例化
class SinglePerson(object):
    def __new__(cls, *args, **kwargs):
        print('SinglePerson.__new__')
        if not hasattr(cls, '_instance'):  # 不存在时创建一次
            # 单下划线也是一个私有属性，只能本文件内访问，双下划线只能本类内访问
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


p = SinglePerson()
p2 = SinglePerson()
p3 = SinglePerson()
print(id(p), id(p2), id(p3))
print(p is p2 is p3)  # is 属于id比较
