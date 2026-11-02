# 长方形
for i in range(1, 8):  # 7行
    for j in range(5):  # 一行5个
        print('*', end='\t')
    print()

print()

# 平行四边形
for i in range(1, 8):  # 7行
    print(end=' ' * i)  # 单行前部空格
    for j in range(5):  # 一行5个
        print('*', end=' ')
    print()

print()

# 三角形
max = 10
for i in range(1, max):  # max行
    print(end='  ' * (max - i))  # 单行前部空格，每列递减1
    for j in range(1, i * 2):  # * 1、3、5、7....
        print('*', end=' ')
    print()

print()

# 空心三角形,不打印的剪掉即可
max = 5
for i in range(1, max):  # max行
    print(end='  ' * (max - i))  # 单行前部空格，每列递减1
    for j in range(1, i * 2):  # * 1、3、5、7....
        if i == 1 or i == max - 1:
            print('*', end=' ')
        else:
            print(f'*' if (j == 1 or j == i * 2 - 1) else ' ', end=' ')

    print()
