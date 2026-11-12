# 采用类来定义一个元类，
# 需求：修改类属性名由小写改为大写,不修改私有属性__attr


# 通过继承type完成
class UpperMetaclass(type):

    # 重写__new__函数 做属性修改
    def __new__(cls, class_name, class_parents, attr_dict):
        # 三目运行+for遍历=生成器generator，然后通过生成器转成可迭代类
        # attrs = 生成器<class 'generator'>
        attrs = ((k, v) if k.startswith('__') else (k.upper(), v) for k, v in attr_dict.items())
        return super().__new__(cls, class_name, class_parents, dict(attrs))


class Person(object, metaclass=UpperMetaclass):
    name = 'lisi'
    __age = 30  # 私有类属性
    pass


# 实例化类对象 私有属性不能直接访问
p = Person()
# print(p.name, p._age)
print(p.NAME)
print(Person.NAME)

print(setattr(Person, 'NAME', '小花'))
print(setattr(Person, '__age', 20))  # setattr可以修改掉私有属性的值
print(getattr(Person, 'NAME'))
print(getattr(Person, '__age'))
print(p.NAME, p.__age)

print(hasattr(Person, '__age'))
print(hasattr(Person, '__AGE'))
