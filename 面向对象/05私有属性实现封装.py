# python没有绝对的私有关键字，通过 __属性 实现隐藏效果
class Girl:

    def __init__(self):
        self.__age = None

    # 合理暴露
    def get_age(self):
        return self.__age

    # 合理暴露
    def set_age(self, age):
        self.__age = 18 if age > 18 else age


girl = Girl()
girl.set_age(19)
print(girl.get_age())
