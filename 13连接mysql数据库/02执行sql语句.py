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

# # -查
# select_sql = "select * from t_book"
# print(cursor.execute(select_sql))
# # 获取表中所有数据，必须执行查询语句：execute
# print(cursor.fetchall())

try:
    # -增单条
    # insert_sql = "insert into t_book values(%s,%s,%s,%s)"
    # args = (0, 'python', 'wjh', 19.99)
    # print(cursor.execute(insert_sql, args))

    # -增批量
    # insert_sql = "insert into t_book values(%s,%s,%s,%s)"
    # args = [(10, 'python10', 'wjh1', 19.99),
    #         (11, 'python20', 'wjh2', 19.99),
    #         (12, 'python30', 'wjh3', 19.99)
    #         ]
    # print(cursor.executemany(insert_sql, args))

    # -修改,后面一定需要条件，不然会修改所有的数据
    # update_sql = "update t_book SET name = %s WHERE id = %s"
    # args = ('python100', 10),
    # print(cursor.execute(update_sql, args))

    # -删除,后面一定需要条件，不然会删除表中所有的数据
    # delete_sql = "delete from t_book WHERE id = %s"
    # args = (0),  # 删除：id=0的所有数据
    # print(cursor.execute(delete_sql, args))

    # -查询 尽可能的控制查询数据的大小，控制内存
    select_sql = "select name,author,price from t_book WHERE price > %s"
    args = (50),  # 查询价格>20的
    print(cursor.execute(select_sql, args))  # 共5条
    print(cursor.fetchone())  # 取出来1条
    print(cursor.fetchmany(2))  # 指定取出来2条
    print(cursor.fetchall())  # 取出来剩下的

    # 增删改需要提交
    connect.commit()
except Exception as e:
    print(e)
    # 语句出错后进行回滚
    connect.rollback()

# if rowcount2 > 0:
#     print('查询成功')
# else:
#     print('查询失败')

# [5]关闭游标
cursor.close()

# [6]关闭connect
connect.close()
