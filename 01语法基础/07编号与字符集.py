# 我爱你-> 001002003
# 码表就叫字符集,每个字对应的码，编码->解码
# unicode 国际通用字符集 三种：utf-8、utf-16、utf-32, python默认为：utf-8

a = '您好python'
b = '您好python'
c = '您好python'
print(a, b, c)  # 能打印出来是因为告诉了编译器解码方式为 utf-8
