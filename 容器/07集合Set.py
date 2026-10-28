# set 也是用{}花括号初始化，只存放value的dict
# 集合中只能存放不可变类型数据
# 容器的值唯一的、乱序的(添加进去时乱序增加，后面不再变)

set1 = set()
set1 = {'a', 1, 'k'}
print(set1)

set1 = set("123456")  # 通过字符串方式创建
print(set1)
set1 = set((1, 2, 3, 4, 5, 6))  # 通过元组方式创建
print(set1)
set1 = set([100, 102, 1, 2, 3, 4, 5, 6])  # 通过列表方式创建
print(set1)

print(1 in set1)  # 是否存在容器中
print(1 not in set1)  # 是否不存在容器中

# 新增为app() 容器元素不能重复
set1.add(10)
set1.add(10)
set1.update([11, 12])  # 通过更新操作来新增
# set1.remove(99) # 删除指定元素 若元素不在会报错的
set1.discard(99)  # discard 删除指定元素 若元素不在不会报错
set1.add(10)
print(set1)
result = set1.pop()  # pop移除，删除内容作为返回结果
print(result)
result = set1.pop()  # pop移除，删除内容作为返回结果
print(result)
print(set1)

set2 = set()
# result = set2.pop()  # 空set pop移除，会报错
# print(result)
