# 案例三 检索匹配所有 .py后缀 文件名
# 要求：文件名 整体包含字母、数字、下划线
import re
from functools import reduce

# \b 单词边界会把空格过滤掉
result = re.findall(r'\w+.py\b', '1.py 2.png 4.txt 5.video 6.py 77.py  99.jpg ')
print(result)

# 案例三 邮箱验证
# 条件： 字母开头+5-10位+@+网易｜qq
print("===============[邮箱验证]")
emailPattern = r'^[a-zA-Z]\w{4,9}@(163|qq)\.(com|cn)$'
print(re.match(emailPattern, 'jsidofj@163.com'))
print(re.match(emailPattern, 'jsid@163.com'))
print(re.match(emailPattern, 'jsid9@162.com'))
print(re.match(emailPattern, 'jsid10@qq.com'))
print(re.match(emailPattern, 'jsid10@qq.cn'))
print(re.match(emailPattern, '100jsid10@qq.cn'))
print(re.match(emailPattern, '100jsid10qq.cn'))

# 案例四 座机号码
# 条件： 区号3-4位-号码8位
print("===============[座机号码]")
# phonePattern = r'\d{3,4}-\d{7}$'  #方法1
phonePattern = r'(\d{3}|\d{4})-(\d{7})$'  # 方法2
print(re.match(phonePattern, '0359-7225185'))
print(re.match(phonePattern, '035-7225185'))
print(re.match(phonePattern, '0359--7225185'))
print(re.match(phonePattern, '-037225185'))

# 案例五 提取标签内的内容
# 条件： <name>内容<name/> name不能为空，内容任意字符空或无限
print("===============[提取标签内的内容]")
result = re.match(r'<(\w+)>(.*)</(\1)>', '<html>hello word</html>')
print(result.groups())  # 表达式中有几组分隔，就会返回几组数据  输出： ('html', 'hello word', 'html')
print(result.group(2))  # 输出：hello word

# 方法2 通过分组别名提取到内容
# result2 = re.match(r"<(?P<tname>\w+)>(?P<msg>.*)</(?P=tname)>", '<html>hello word</html>')
result2 = re.match(r"<(\w+)>(?P<msg>.*)</(\1)>", '<html>hello word2</html>')
print(result2.group('msg'))  # 输出：hello word2

# 案例六 提取字符串中 所有的数字然后相加 数字包括正负、小数
# 条件：-3.14
print("===============[提取字符串中所有数字然后计算和]")
result_lis = re.findall(r'-?\d+\.?\d*', 'ppp1ppp-9aaa9.88 99.00ppp')
print(result_lis)
initV = -0.88  # 初始值，从-0.88开始加
print(reduce(lambda a, b: float(a) + float(b), result_lis, initV))  # 100.88

# 案例七 匹配整个字符串中是否是整数或小数
# 条件：包含+-、也可没有
print("===============[匹配整个字符串中整数或小数]")
# num_pattern = r'(-?|\+?)\d+\.?\d*' # 方法1  (-?|\+?) == [+-]?
num_pattern = r'[+-]?(0|[1-9]\d*)(\.\d+)?'  # 方法2  注意：(0|[1-9]\d*) 用来解决：-03.14的问题
print(re.fullmatch(num_pattern, '+3.14'))
print(re.fullmatch(num_pattern, '-3.14'))
print(re.fullmatch(num_pattern, '-03.14'))
print(re.fullmatch(num_pattern, '-3.'))  # (\.\d+)?  .num 是一组 这一组整体 无或最多1个
print(re.match(num_pattern, '3.14 xxx'))
print(re.fullmatch(num_pattern, '3.14 xxx'))  # fullmatch 表示整个串 不会切割匹配

# 案例8 获取字符串所有中文内容
# 中文在国际编码的范围：\u4e00-\u9fa5
print("===============[获取字符串所有中文内容]")
print(re.findall(f'[\u4e00-\u9fa5]+', 'kk ll阿里 jheo小强== +哈哈'))  # 输出：['阿里', '小强', '哈哈']
