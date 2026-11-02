# 键值对，key:value dict ,key为唯一不可变的， value：啥都可以存，操作只能通过key去操作
# del、update、clear、pop有删除结果
d = {} # 花括号初始化
d['a'] = 1
d[100] = 2
print(d)
rsult = d.pop('a', '删除失败')
print(d)
print(rsult)
print(type(d))

dd = dict(name='zhangsan', age=22, )
print(type(dd))
print(dd)

ddd = dict([('name', '小明'), ('age', 22)])
print(type(ddd))
print(ddd)

dict4 = dict.fromkeys(['name', 'age'])  # 定义key,value默认为none类型
dict4['age'] = 30
print(type(dict4))
print(dict4)

# 遍历操作：
for key in dict4:
    print(key, end='、')

print()

for key, value in dict4.items():
    print(key, value, end='、')

print()
for key in dict4.keys():
    print(key, end='、')

print()
for value in dict4.values():
    print(value, end='、')
