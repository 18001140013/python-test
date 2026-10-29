# 将函数赋值给变量
def hello():
    print('hello world')


func = hello
# 现在变量func 等价于 hello
func()
print(func is hello)  # is 为身份运算符 判断这两个是否指向同一个对象
print(hello is func)

print(type(func))
print(type(hello))
