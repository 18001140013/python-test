# 比较运算符也叫关系运算符，用于条件判断，结果一定是布尔值
a, b = 10, 20
print(a == b)

s1, s2 = 'a', 'b' # unicode码比较，有要有1位比较出来就不会比较后面的了
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)
print(ord(s1), ord(s2))
print(1 == True)
m = None
s = 1
s2 = False
print(m is True)
print(m is False)
print(s == True)
print(s2 is False)