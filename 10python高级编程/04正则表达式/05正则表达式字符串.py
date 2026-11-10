# 正则表达式是由普通字符（例如字符 a 到 z）以及特殊字符（称为 "元字符"）组成的匹配模式。
# 作用是：在搜索文本时要匹配的一个或多个字符串。
# 正则表达式作为一个匹配模式，所搜索的字符串进行匹配。
import re

# 元字符	功能：
# .	    匹配任意单个字符（不包括换行符）
# []	匹配字符集，区间中的集合，可匹配其中任意一个字符
# \d	匹配数字，即 0-9，可以表示为 [0-9]
# \D	匹配非数字，即不是数字，相当于 [^0-9]
# \s	匹配空白字符，即 空格，tab 键，相当于 [\t\n\r\f\v]
# \S	匹配非空白字符，相当于 [^\t\n\r\f\v]
# \w	匹配单词字符，即 a-z、A-Z、0-9、_
# \W	匹配非单词字符，即非数字、字母、下划线中的任意字符，相当于 [^\w]

# 核心规则再复述一遍：
# `* + ?` 默认修饰**紧挨着它前面那 1 个东西**；
# 这个 “东西” 有两种：
# ① 单个字符（比如 `a`、`\d`、`[0-9]`）
# ② 一个分组 `(...)`

# 匹配多个字符的相关格式：
# 字符：	功能：
# *	    匹配前一个字符出现 0 次或者无限次，即可有可无
# +	    匹配前一个字符出现 1 次或者无限次，即至少有 1 次
# ?	    匹配前一个字符出现 1 次或者 0 次，即要么有 1 次，要么没有
# {m}	匹配前一个字符出现 m 次
# {m,}	匹配前一个字符至少出现 m 次
# {m,n}	匹配前一个字符出现从 m 到 n 次

# 写法	被修饰对象	含义
# ab+	单个字符 b	a 后面，b 重复多次
# (ab)+	分组 (ab)	ab 这个整体重复多次
#
# 没有括号，符号管前面**一个字符**；
# 有括号，符号管括号里面**一整个分组**。

# 固定：138 分组：-数字(至少1个数字) 分组限制：至少1个-数字
print(re.search(r'138(-\d+)+', "138  138-123456-10  138- 138-0"))  # 输出：'138-123456'
print(re.search(r'138(-\d+)?', "138  138-123456-10  138- 138-0"))  # 输出：'138'

# 区分
print(re.search(r'(ab)+', "abb ab ababab"))  # 输出：'ab'
print(re.findall(r'(ab)*?', "abbabababab"))  # 输出：'ab' 5次
print(re.findall(r'(ab)*+', "abbabababab"))  # 输出：'ab'2次

# 区分
print(re.search(r'ab+c', "abbbbc abc ac"))  # 输出：'abbbbc'
print(re.search(r'ab*c', "abbbbc abc ac"))  # 输出：'abbbbc'
print(re.search(r'ab?c', "abbbbc abc ac"))  # 输出：'abc'

# 区分
print(re.findall(r'ab+c', "abbbbc abc ac"))  # 输出：['abbbbc','abc']
print(re.findall(r'ab*c', "abbbbc abc ac"))  # 输出：['abbbbc','abc','ac']
print(re.findall(r'ab?c', "abbbbc abc ac"))  # 输出：['abc','ac']

# [] 代表了一个区间字符集
print(re.search(r'[a-zA-Z]', "abc ac 123"))  # 输出：'a'
print(re.findall(r'[a-zA-Z]', "abc ac 123"))  # 输出：['a', 'b', 'c', 'a', 'c']
print(re.findall(r'[r\d]', "abc ac 123"))  # 输出：['1', '2', '3']
print(re.findall(r'[a-zA-Zr\d]', "abc ac 123"))  # 输出：['a', 'b', 'c', 'a', 'c', '1', '2', '3']

# 邮箱
content = """
客服邮箱：service@shop.com
个人邮箱：zhang-san.123@qq.com
无效邮箱：abc@、abc@.com
test:a@b.c
test:a@b-c
test:a@b.c-
test:a@b.c_
"""
email_pattern = r"[\w.-]+@[\w.-]+\.\w+"  # 注意：.本身是一个元字符功能：任意一个字符， \.转义之后->普通点
print("提取到邮箱：", re.findall(email_pattern, content))

# 匹配多个限制
#   *：{0,}
#   +：{1,}
#   ?:{0,1}
strData = """
1：service@shop.com
2：zhang-san.123@qq.com
3：abc@、abc@.com
4:a@b.c
5:a@b-c
"""
email_pattern = r"[\w.-]+@[\w.-]{2,}\.\w+"  # {2,} 标示至少2个及以上
# 输出：['service@shop.com', 'zhang-san.123@qq.com']
print("提取到数据：", re.findall(email_pattern, strData))

# 这里的[a-z] 默认为1个字符{1,1} = {1}
print(re.search(r'[a-z]\d+', "aaaa123"))  # 输出：'a123'
