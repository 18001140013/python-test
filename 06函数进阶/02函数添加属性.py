# 函数添加属性

def hello():
    print("hello")

hello.author = 'wjh'
hello.version = '3.0'
hello.dec = '这是一个测试函数'

print(hello.author)
print(hello.version)
print(hello.dec)