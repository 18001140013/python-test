# 列表遍历方式：
lis = [4, 5, 6, 7, 8, 9, ]

# 方法1:
for item in lis:
    print(item, end='')

# 方法2:
print()
index = 0
while index < len(lis):  # len函数 取出长度length
    print(lis[index], end='')
    index += 1

# 方法3 列举或枚举enumerate:
print()
for index, chart in enumerate(lis):  # 下标与内容同时遍历
    print(f'下标：{index}', f',内容：{chart}', end=';\t')

print()
# 方法4 range():
for index in range(len(lis)):
    print(f'下标：{index}', f',内容：{lis[index]}', end=';;\t')

print()
# 方法5 倒序reversed():
for chart in reversed(lis):
    print(chart, end=';\t')

print()
# 方法6 切片实现倒序:
for item in lis[::-1]:
    print(item, end=';;\t')
