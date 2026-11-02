# str 方法重写
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'{self.name}, {self.age}'


p = Person(name='小红', age=19)
print(p)  # 重写后，打印对象，可以找见是哪个对象
