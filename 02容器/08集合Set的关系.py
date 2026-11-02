# set函数：
# set1.difference(set2)
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 8, 9, 100, 200, 300}
print(set1)
print(set2)

# 求差异结果
result = set1.difference(set2)
print(f'求差异结果：{result}')
print(set1)

# 求差异结果并赋值给set1
result2 = set1.difference_update(set2)
print(f'求差异 并更新：{result2}')
print(set1)

# 求并集 合并&去重复
set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set4 = {1, 2, 8, 9, 100, 200, 300}
print(f'求并集 ：{set3.union(set4)}')

# 是否为子集  子.issubset(父)
# 是否为超集  父.issuperset(子)
set5 = {1, 2, 3, 4, 5, 6, 7, 8, 9} 
set6 = {1, 2, 8, 9, 100, 200, 300}
set7 = {1, 2, 8, 9}
print(f'是否为子集1 ：{set6.issubset(set5)}')  # false
print(f'是否为子集2 ：{set7.issubset(set5)}')  # true

print(f'是否为超集1 ：{set5.issuperset(set6)}')  # false
print(f'是否为超集2 ：{set5.issuperset(set7)}')  # true

# 是否无交集，一个都没有 a.isdisjoint(b) ,无交集返回：true
set8 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set9 = {1, 2, 8, 9}
set10 = {10, 11, 12}
print(f'是否无交集1 ：{set8.isdisjoint(set9)}')  # false
print(f'是否无交集2 ：{set8.isdisjoint(set10)}')  # true
