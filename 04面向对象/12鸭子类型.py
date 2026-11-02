#### 鸭子类型：java是静态语言，python属于动态语言，不用父类也行

#     子类 狗
class Dog():
    def speak(self):
        print('小狗汪汪叫')


#     子类 猫
class Cat():
    def speak(self):
        print('小猫喵喵叫')


# 这样也行，animal 是动态的
def animal_speak(animal):
    animal.speak()


animal_speak(Dog())
animal_speak(Cat())
