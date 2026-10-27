# 键盘输入体重、身高 BMI = 体重（kg）/身高（米）
w = float(input('请输入体重：'))
h = float(input('请输入身高：'))

print(f'你的体重是：{w} 公斤,你的身高是：{h} 米')

BMI = w / h
# BMI = 42.857
print('%.1f'%BMI)  # 占位符
print('你的体脂率是：%.2f' % BMI)  # 占位符 四舍五入
print('你的体脂率是：%.3f' % BMI)  # 占位符
