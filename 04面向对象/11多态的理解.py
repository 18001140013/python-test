#### 多态的理解: 同一个方法，不同的对象调用，表现出不同的行为 用途：耦合性更低
#     父类  动物
class Animal:
    def speak(self):
        pass


#     子类 狗
class Dog(Animal):
    def speak(self):
        print('小狗汪汪叫')


#     子类 猫
class Cat(Animal):
    def speak(self):
        print('小猫喵喵叫')


# 函数定义，接受一个动物，这里的动物可以是小猫、小狗，就叫多台
# 多态=同一个方法，不同的对象调用，表现出不同的行为，新增一个对象（也就是新增一个行为）不影响其他地方代码
def animal_speak(*, animal: Animal):
    animal.speak()


animal_speak(animal=Dog())
animal_speak(animal=Cat())
