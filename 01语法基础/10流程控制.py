# 流程控制语句是用来控制程序各语句的执行顺序
# 控制语句：顺序、选择、循环结构
# 完成猜数游戏

# 分支：
a = 4
price = 1000
if a > 3:
    print("满足，可以上幼儿园")
    if price > 800:
        print("可以优惠200")
elif a > 8:
    print("太大了，不可以上幼儿园")
else:
    print("不满足，不能上幼儿园")

# 判断一个数是偶数还是奇数
b = 10
if b % 2 == 0:
    print("偶数")
else:
    print("奇数")

# 三目条件运算符 替代if else成为一句代码
print(f'偶数' if b % 2 == 0 else '奇数')

# 循环：while、for
num = 0
sum = 0
while num < 3:
    num += 1
    sum = sum + num

print(f"总和：{sum}")

for num in range(1, 6):  # 界限函数，包头不包尾  打印1-5
    print(f"num1：{num}")

for num in range(5):  # 0、1、2、3、4
    print(f"num2：{num}")

for num in range(1, 10, 2):  # 1,3,5,7,9
    print(f"num3：{num}")

for s in 'abcdef':  # 字符串迭代
    print(f"s：{s}")

# 计算1-100奇数之和：
sum = 0
sum2 = 0
# 方式1
for num in range(101):
    if num % 2 == 1:
        sum += num
print(f"1 1-100奇数之和：{sum}")

# 方式2
for num in range(1, 100, 2):
    sum2 += num
print(f"2 1-100奇数之和：{sum2}")

# 方式3
sum3 = 0
num = 1
while True:
    if num <= 100:
        sum3 += num
    else:
        break
    num += 2

print(f"3 1-100奇数之和：{sum3}")

# 方式4
sum4 = 0
num = 1
while num <= 100:
    sum4 += num
    num += 2

print(f"4 1-100奇数之和：{sum4}")

# break、continue
for num in range(5):
    if num == 3:
        break
    print(f"测试break：{num}")

for num in range(5):
    if num == 3:
        continue
    print(f"测试continue：{num}")
