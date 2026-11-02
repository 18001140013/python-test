# 9*9乘法口诀： 1->9 递加1
for i in range(1, 10, 1):
    jMax = i + 1
    for j in range(1, jMax):
        print(f'{j}x{i}={j * i}', end='\t')
    print()

print()

# 9*9乘法口诀 上下倒过来：9->1 递减1
for i in range(9, 0, -1):
    jMax = i + 1
    for j in range(1, jMax):
        print(f'{j}x{i}={j * i}', end='\t')
    print()

print()
# 9*9乘法口诀 对称倒过来：9->1 递减1
for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print(f'{j}x{i}={j * i}', end='\t')
    print()
