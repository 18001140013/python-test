# 元组定义
tt = tuple
tt = (1, 2, 34, 5)
print(type(tt))
tt = (1)  # 会认为是int类型，需要增加逗号
print(type(tt))
tt = (1,)
print(type(tt))
print(tt)

# 查看 与列表没啥区别，常用的操作都可以用，结构一个是[] 一个是()
# ###### del tt[0] 会报错，元组不能修改与删除，用来存放固定不变的数据， 不能增删改，只能查
# 列表随便改，用来存经常变动的数据，list可变、tuple不可变
tt = (1, 2, 34, 5, (10, 20, 30))
print(tt[len(tt) - 1][2])

lst = [1, 2, 34, 5, [10, 20, 30]]
print(tt[len(tt) - 1][2])
