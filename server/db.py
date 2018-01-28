from pymysql import connect

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

    def create_update_delete(self,sql,params):
        count = 0
        try:
            self._connect()
            count = self.cursor.execute(sql,params)
            self.conn.commit()
            self._close()
        except Exception as e:
            print(e)
        return count

if __name__ == '__main__':
    pass