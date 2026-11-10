# 正则表达式目的：用来去一个大的字符串中找到或检索想要的字符数据
# 系统包：re模块
# findIter:匹配，从任意一个位置开始匹配，匹配不到返回空迭代器,匹配到继续检索，直到检索结束，返回所有匹配值为一个迭代器
import re

str = '123python123python456python789'
str2 = '123789'
result = re.finditer('python', str)
for item in result:
    print(f'配置结果：{item.group()},{item.span()}')
