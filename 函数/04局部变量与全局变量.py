# 局部参数与全局参数的使用
def fun1():
    num = 10  # 函数内的叫局部变量，调完函数后，内存释放
    print(num)
    global num2  # 函数内修改局部参数 若不global 无法修改
    num2 = 13
    print(num2)


num2 = 12  # 全局变量，范围更大

print(num2)
fun1()
print(num2)

# 函数调用函数叫：嵌套函数
