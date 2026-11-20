# [pymysql库下载]：
# pip install pymysql
# pip show pymysql

# [1] 导入mysql
from pymysql import *

# [2]创建connect 连接mysql
connect = Connect(host='localhost', port=3306, user='root', password='root', db='demo', charset='utf8')

# [3]创建游标对象
cursor = connect.cursor()

# [4]执行sql语句 - 操作mysql

name = input('输入书名：')

# 写法1
# sql = "select * from t_book where name='%s'"%(name) # sql 注入 输入的name混合了sql语句 有漏洞，所以使用参数类型访问
# rowcount = cursor.execute(sql)

# 写法2
sql2 = 'select * from t_book where name=%s'
rowcount2 = cursor.execute(sql2, (name,))
print(rowcount2)

if rowcount2 > 0:
    print('查询成功')
else:
    print('查询失败')

# [5]关闭游标
cursor.close()

# [6]关闭connect
connect.close()
