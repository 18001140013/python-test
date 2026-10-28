# 类型转化
str = 'abdcdefg'
lis = list(str)
print(lis)
tlp = tuple(lis)
print(tlp)
lis = list(tlp)
print(lis)
print(tuple(range(1, 10)))  # range也不包含尾 1-9
