from MysqlHelper import *

'''
    创建db操作类
'''
my_sql_helper = MysqlHelper(connect_param=MysqlHelper.connect_param1)

'''
    查询数据
'''
# select_sql = "select name,author,price from t_book WHERE price > %s"
#
# print(f'查询一条数据：{my_sql_helper.get_one(select_sql, (50,))}')
#
# result = my_sql_helper.get_all(select_sql, (50,))
# print(f'查询多条数据：{result}')
#
# # 遍历打印：
# for item in result:
#     print(item)

'''
    增加
'''
# -增1条
# insert_sql = "insert into t_book values (%s,%s,%s,%s)"
# args = (0, 'python', 'wjh', 19.99)
# print(f'增加单条：{my_sql_helper.insert(insert_sql, args)}')

# -增批量
# args = [(100, 'python100', 'wjh100', 19.99),
#         (110, 'python200', 'wjh200', 19.99),
#         (120, 'python300', 'wjh300', 19.99)
#         ]
# print(f'增加多条：{my_sql_helper.insert_many(insert_sql, args)}')

'''
    修改
'''
# update_sql = "update t_book set price = %s where id > %s"
# args = (99.99, 5)
# print(f'修改了 {my_sql_helper.update(update_sql, args)} 条数据')

'''
    删除
'''
delete_sql = "delete from t_book where id > %s and id < %s"
args = (10, 100)
print(f'删除了 {my_sql_helper.delete(delete_sql, args)} 条数据')
