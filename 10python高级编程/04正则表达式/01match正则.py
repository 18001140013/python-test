# 正则表达式目的：用来去一个大的字符串中找到或检索想要的字符数据
# 系统包：re模块
# match:匹配，从起始位置开始匹配，匹配不到返回none,匹配到停止检索，返回第一条。
import re

str = 'python123python456python789'
result = re.match('python', str)
if result is not None:
    print(f'匹配第一条数据的坐标位置：{result.span()}')
    print(f'匹配第一条数据的值：{result.group()}')
else:
    print('匹配失败', result)
