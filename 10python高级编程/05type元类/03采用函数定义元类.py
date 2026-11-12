# 采用函数定义元类，自定义一个元类metaclass,创建类对象时修改类属性
# 需求：类的创建由type创建，我们通过metaclass手动来创建这个类,然后修改类属性名由小写改为大写,不修改私有属性_attr

# 定义一个metaclass，代码会在加载时执行，创建了Person类对象
# result: type 元类的根是type
def upper_metaclass(class_name: str, class_parents: tuple, attr: dict):
    attr_new = {}
    for k, v in attr.items():  # 字典遍历 k、v,通过函数items()
        k_str = str(k)
        attr_new[k if k_str.startswith('__') else k_str.upper()] = v

    print(attr)
    print(attr_new)

    return type(class_name, class_parents, attr_new)


class Person(object, metaclass=upper_metaclass):
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
