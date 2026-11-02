name = "小明"
age = 30
print("我的名字：%s" % name)
print("我的名字：%s，我的年龄：%d" % (name, age)) # 多个占位符打印

num = 12345
print('我的工资是%09d' % num)  # 0000123456 用0补全

pie = 3.1415926
print("圆周率：%.3f" % pie)  # 3.142 四舍五入操作保留

st1 = "10"
st2 = "90"
print(st1, end=",")  # 用，替代换行符
print(st2)

st3 = st1 + "," + st2
print(st3.split(","))  # 逗号分隔成数组['10','90']
