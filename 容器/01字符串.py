############# 下标 正向索引与反向索引
s1 = 'abcdefghijklmnopqrst'
print(s1[3])
print(s1[-2])

############# 切片操作 意思：字符串剪切， 使用：开始位置:结束位置:步长 ，特点：包头不包尾
print(f"切片1：{s1[2:5:1]}")  #
print(f"切片2：{s1[2:5]}")  # size默认步长为：1
print(f"切片3：{s1[:5]}")  # 0:5:1 start:end:size , 开始：默认下标0
print(f"切片4：{s1[1:]}")  # 1:max:1     尾部：默认为最后1位
print(f"切片5：{s1[::2]}")  # 0:max:2
print(f"切片6：{s1[:-1]}")  # 0:-1:1 ,-1=尾部max-1
print(f"切片7：{s1[-4:-1]}")  # -4:-1:1 ,-4->-1 的位置 -4 -3 -2 ，qrs
print(f"切片8：{s1[::-1]}")  # 0:max:-1,从尾->头 步长1， 变成了倒序

############# 字符串常用的方法：
print(f"方法1：{s1.find("de")}")  # 3 找下标，找不到不报错
print(f"方法2：{s1.index("de")}")  # 3 找下标，找不到就报错
s = "abc de"
print(f"方法3：{s.split(" ")}")  # 字符串切割成数组
print(f"方法4：{s.replace("abc", 'abc1')}")  # 字符串替换，替换后全部输出，找不到，原样输出
print(f"方法5：{s.count("abc")}")  # 字符串计数次数 1

############ 字符串遍历 ############
# 方法1:
ss = 'python'
for chart in ss:
    print(chart, end='')

print()
# 方法2:
index = 0
while index < len(ss):  # len函数 取出长度length
    print(ss[index], end='')
    index += 1

print()
# 方法3 列举或枚举enumerate:
for index, chart in enumerate(ss):  # 下标与内容同时遍历
    print(f'下标：{index}', f',内容：{chart}', end=';\t')

print()
# 方法4 range():
for index in range(len(ss)):
    print(f'下标：{index}', f',内容：{ss[index]}', end=';;\t')

print()
# 方法5 倒序reversed():
for chart in reversed(ss):
    print(chart, end=';\t')

print()
# 方法6 切片实现倒序:
for chart in ss[::-1]:
    print(chart, end=';;\t')
