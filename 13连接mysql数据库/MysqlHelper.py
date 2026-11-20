from pymysql import *

'''
    封装一个数据库操作类
    避开connect、cursor多次创建与关闭，避开函数多次调用
'''


class MysqlHelper(object):
    # 参数1
    connect_param1 = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'demo',
        'charset': 'utf8',
    }

    def __init__(self, connect_param):
        self.__host = connect_param['host']
        self.__port = connect_param['port']
        self.__user = connect_param['user']
        self.__password = connect_param['password']
        self.__db = connect_param['db']
        self.__charset = connect_param['charset']

    def __connect(self):
        # 连接sql
        self.__conn = Connect(host=self.__host,
                              port=self.__port,
                              user=self.__user,
                              password=self.__password,
                              db=self.__db,
                              charset=self.__charset)

        # 创建游标
        self.__cursor = self.__conn.cursor()

    def __close(self):
        self.__cursor.close()
        self.__cursor = None
        self.__conn.close()
        self.__conn = None

    # 获取一条数据
    def get_one(self, sql, args):
        result = None
        try:
            self.__connect()
            self.__cursor.execute(sql, args)
            result = self.__cursor.fetchone()
            self.__close()
        except Exception as e:
            print(e)
        return result

    # 获取所有数据
    def get_all(self, sql, args):
        result = ()  # 元组
        try:
            self.__connect()
            self.__cursor.execute(sql, args)
            result = self.__cursor.fetchall()
            self.__close()
        except Exception as e:
            print(e)
        return result

    # 增加-1条
    def insert(self, sql, args):
        return self.__edit(sql, args, )

    # 增加-批量
    def insert_many(self, sql, args, ):
        return self.__edit(sql, args, is_many=True)

    # 修改
    def update(self, sql, args):
        return self.__edit(sql, args)

    # 删除
    def delete(self, sql, args):
        return self.__edit(sql, args)

    # 写数据操作具体实现，增删改都用这个函数来操作
    def __edit(self, sql, args, is_many: bool = False):
        result = 0
        try:
            self.__connect()
            result = self.__cursor.executemany(sql, args) if is_many else self.__cursor.execute(sql, args)
            self.__conn.commit()
            self.__close()
        except Exception as e:
            print(e)
            self.__conn.rollback()  # 回滚

        return result
