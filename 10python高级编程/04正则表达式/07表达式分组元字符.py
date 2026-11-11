# 分组元字符
import re

# ｜ 或
# (ab) 将括号中字符作为一个分组
# \number 匹配前面索引一样的字符串
# (?P<name>) 分组起别名
# (?P=name) 引用别名name为分组匹配

# * {0,} 可有可无
print(re.match(r'\w*', 'abcd'))
# 匹配非0数字 或 100
print(re.match(r'[1-9]+$|100|200', '200'))
# 匹配至少1个ab
print(re.search(r'(ab)+', 'bbbbabab'))
# 匹配一个邮箱：首字母为字符、4-20位数字、@、（163|qq）.com
print(re.match(r'[a-zA-Z][0-9]{4,20}@(163|qq)\.com', 'A1234@qq.com'))
# 匹配一个邮箱：用户名单词字符4-20位、@、（163|qq）.com
print(re.match(r'\w{4,20}@(163|qq)\.com', '1234@qq.com'))
# 匹配是一个网页标签 <html>hello word</html> ,通过\1反向引用第一组捕捉到的内容。 .*?=解释：.：任意字符包含空格 *：无或无限 ?：非贪婪 遇到闭合标签就停掉了
print(re.match(r'<([a-zA-Z]+)>.*?</\1>', "<html>hello word</html>word</html>"))

# 使用分组起别名，引用别名方式 匹配 网页标签 定义：(?P<分组别名>[匹配模式]) 引用：(?P=分组别名)
print(re.match(r'<(?P<tname>[a-zA-Z]+)>.*?</(?P=tname)>', "<html>hello word</html>word</html>"))
