# 正则表达式边界元字符，就是限制以什么开始以什么结束的元字符
# ^a 匹配以a为开始，多行模式下会取每行的开始（也是取返的意思应用不同场景）
# a$ 匹配以a为结尾
# \b 匹配一个单词的边界
# \B 匹配一个非单词边界

import re

content = '''a123abc789a3rb\n
adddddb
abffffab
'''

# ^ 放[]外边是 匹配以什么开始的
print(re.findall(r'^[a-zA-Z]+@[0-9]+.com', 'abc@999.com'))  # 输出: ['abc@999.com']
# ^ 放[]里边取反，匹配以非数字的
print(re.findall(r'[^0-9]+', '--a0c--'))  # 输出: ['--a', 'c--']

# $a 匹配a结尾的
print(re.findall(r'[0-9]+a$', '33aa 123a'))  # 输出: ['123a']

# \b 从单词边界开始匹配
print(re.findall(r'\b\w+\b', '---- abc999d3 -----'))  # 输出: ['abc999d3']
