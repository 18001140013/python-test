# 算术运算符
print(1 + 4)  # + 5
print(4 - 1)  # - 3
print(2 * 4)  # * 8
print(7 / 3)  # 除法结果为符点数 7/3=2.3333333
print(7 // 3)  # 整除 向下取整 7/3=2
print(7 % 3)  # 取余（求模） 7%3=1
print(2 ** 4)  # 幂运算 2*2*2*2=16

print(16 ** 0.5)  # 幂运算- 平方根：4
print(4 ** 0.5)  # 幂运算- 平方根：2
print(4 ** (1 / 2))  # 幂运算- 平方根：2

print(27 ** (1 / 3))  # 幂运算- 立方根：3
print(64 ** (1 / 3))  # 幂运算- 平方根：4
print(125 ** (1 / 3))  # 幂运算- 平方根：5

# 幂运算：** = pow()函数
print(pow(125, 1 / 3))  # 幂运算- 平方根：5
print(pow(4, 3))  # 幂运算- 平方根：4*4*4=64

# 赋值运算符 = 就是等号
x = y = z = 100
x, y = 10, 20

# 交换
m = 10
n = 30
print("交换前：m:", m, "n:", n)
m, n = n, m
print("交换后：m:", m, "n:", n)

# 复合赋值运算符
a = 10
a += 2
print(a)  # 运算后再赋值的操作


# None类型：空类型
def add():
    print("add")


print("类型", type(add()))

n = None
print("类型值:", n, "type:", type(n))

# 类型转换：布尔值
n1 = 0
n2 = 19
print(bool(n1), bool(n2))
s1 = ""
s2 = "sss"
print(bool(s1), bool(s2))

# 转义占： \r回车
mm = 'mmmmmm'
nn = "nnnnnn"
print(mm + "\r" + nn)

# 转义占： \b 退格符,删除前一个符号
mmm = '12345'
nnn = "6789"
print(mmm + "\b" + nnn)

# 转义占： \\ 标识一个反斜杠
print(mmm + "\\" + nnn)

# 转义占： \' , \" 标识一个单引号 , 一个双引号
print(mmm + "\'" + nnn)
print(mmm + "\"" + nnn)

# 转义占： \t' 水平制表符 tab 多个空格
bb = "123"
cc = "789"
print("123456789" * 10)
print(bb + "\t" + cc)
print(bb * 2 + "\t" + cc * 2)
print(bb * 4 + "\t" + cc * 4)
