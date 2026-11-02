# python 支持多继承

class A:
    def a_method(self):
        print('a')


class B:
    def b_method(self):
        print('b')

# C->AB
class C(A, B):
    def c_method(self):
        print('c')


c = C()
c.a_method()
c.b_method()
c.c_method()
