############ 列表
# 列表基本定义
list1 = []
list1 = list()
list2 = [1, 2, 3, 4, 5]
list3 = [1, '2', 3, 4, True, 5.0]
list4 = [1, 2, 3, list2, list3]  # 嵌套

print(f'list1 {list1}', end="\n")
print(f'list2 {list2}', end="\n")
print(f'list3 {list3}', end="\n")
print(f'list4 {list4}', end="\n")
print(f'list4 {type(list4)}', end="\n")

for chart in list4:
    print(chart, end=",\t")

print()
# 列表查询操作-索引
list5 = [1, 2, 3, 4, 5]
print(f'索引 {list5[0]}、{list5[-1]}', end="")  # 1、5
# 列表查询操作-切片
print(f'\n切片 {list5[0::2]}', end="")  # 1、3、5
print(f'\n切片倒序 {list5[::-1]}', end="")  # 5、4、3、2、1

print()
# 列表增加操作-增加元素
list6 = [1, 2, 3, 4, 5]
list6.append(6)  # 向后增加元素
list6.insert(2, 2.1)  # 坐标位置前插入元素
list6.extend('python')  # 追加 延伸：分隔成字符增加到元素
print(f'\n增加元素后遍历： {list6[::1]}', end="")
list6.reverse()  # 反转
print(f'\n增加元素后遍历： {list6[::1]}', end="")

print()
# 列表修改操作-修改元素
list7 = [1, 2, 3, 4, 5]
list7[2] = 'p'  # 指定下标修改
print(f'\n修改元素后遍历： {list7}', end="")
print(f'\n查找元素坐标： {list7.index('p')}', end="")
print(f'\n查元素计数： {list7.count('p')}', end="")
print(f'\n查列表长度： {len(list7)}', end="")

# 列表删除操作-删除元素
list8 = [10, 20, 30, 40, 50, 60]
del list8[2]  # 指定元素删除
print(f'\n删除元素后： {list8}', end="")
list8.pop()  # 删除最后一个,empty 时会报错
print(f'\n删除元素后： {list8}', end="")
list8.remove(10)  # 删除指定内容,内容不在后报错
print(f'\n删除元素后： {list8}', end="")
list8.clear()  # 清空所有内容
print(f'\n删除元素后： {list8}', end="")

# 列表基本函数操作-列表方法函数使用：
list9 = [10, 20, 30, 40, 50, 60, 1]
print(f'\n方法函数 长度： {len(list9)}', end="")
print(f'\n方法函数 最大数： {max(list9)}', end="")
print(f'\n方法函数 最小数： {min(list9)}', end="")
print(f'\n方法函数 求和： {sum(list9)}', end="")
print(f'\n方法函数 从小到大排序： {sorted(list9, reverse=True)}', end="")  # 默认为升序，reverse=true 从大到小排序变为降序
