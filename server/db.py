from pymysql import connect

'''
数据表的设计：
1. 密码不能储存为明文
2. 字段要尽可能简明
3. 数据表储存的是全部用户的相关信息，没有为单一用户建立的数据表

数据库名字：SSLTools
数据表：
特殊字段：
    1. 昵称：用户指定的标识自身的唯一字符
    2. id：与该项目无关、提供给数据库管理

1. 登录历史记录表
    字段：id、昵称、登录IP、登录时间、离线时间
    功能：用户查询
    主键：id
    外键：昵称

2. 用户个人信息表
    字段：id、昵称、真实姓名、性别、工作部门、职位、自我介绍、是否离职、邮箱、电话、密码、是否在线 
    功能：
        1. 登录验证
        2. 注册验证
        3. 供其他用户查询联系

3. 用户通讯历史记录表
    字段：id、发信方昵称、收信方昵称、发送时间、收信方标志、信息内容
    功能：
        1. 用户查询
        2. 管理员查询
'''


class MySqlHelper:
    def __init__(self,user,passwd,db,host = '127.0.0.1',port = 3306,charset = 'utf8'):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.charset = charset
        self.db = db

    def _connect(self):
        self.conn = connect(user = self.user,password = self.passwd
                       ,host = self.host,port = self.port
                       ,charset = self.charset,db= self.db)
        self.cursor = self.conn.cursor()

    def _close(self):
        self.cursor.close()
        self.conn.close()

    def read_one(self,sql,params=()):
        result = None
        try:
            self._connect()
            self.cursor.execute(sql,params)
            result = self.cursor.fetchone()
            self._close()
        except Exception as e: # except Exception e:
                               # This is python 2 usage and is not supported in python 3
            print(e)
        return result

    def read_all(self,sql,params=()):
        result = ()
        try:
            self._connect()
            self.cursor.execute(sql,params)
            result = self.cursor.fetchall()
            self._close()
        except Exception as e: # except Exception e:
                               # This is python 2 usage and is not supported in python 3
            print(e)
        return result

    def execute(self, sql, params = None):
        count = 0
        try:
            self._connect()
            count = self.cursor.execute(sql,params)
            self.conn.onLogin()
            self._close()
        except Exception as e:
            print(e)
        return count

if __name__ == '__main__':
    pass