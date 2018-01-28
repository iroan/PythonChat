from server.db import MySqlHelper
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

class SignIn:
    '''
    如何被使用：
        被server调用、
    :return:

    功能：
    参数：
    返回值：
    '''
    def __init__(self,nickname,password_sha1):
        self.nickname = nickname
        self.password = password_sha1
        self.is_1_Flag = b'\x01'
        self.mysqlhelper = MySqlHelper('iroan','iroanMYS47','ssltools')

    def register(self):
        '''
        输入：昵称、密码
        返回：
            1. 注册失败-因为该昵称已经被使用
            2. 注册失败-程序错误
            3. 注册成功
        :return:
        '''
        sql = 'insert into user(nickName,password) values(%s,%s);'
        res = self.mysqlhelper.create_update_delete(sql,[self.nickname,self.password])
        if res == 0:
            return '注册失败-因为该昵称已经被使用，请换一个昵称注册'
        elif res == 1:
            return '注册成功，请登录使用'
        else:
            return '注册失败-程序错误'

    def singin(self):
        sql = 'select isOnline,password from user where nickName = %s;'
        res = self.mysqlhelper.read_all(sql,[self.nickname]) # TODO isOnline要设置默认值0
        # 'navicat 设置索引中的名是什么意思、有什么作用'
        if res == ():
            return '该用户未注册'

        isonline = res[0][0]
        password = res[0][1]

        if password == self.password:
            if isonline == self.is_1_Flag:
                return '该用户已登录，不能重复登录' # TODO 需要支持重复登录吗？
            if isonline != self.is_1_Flag:
                self._update_info()
                return '登录成功'
        else:
            return '密码错误'
    def _update_info(self):
        '''
        更新内容：
            1. 用户在线字段
            2. TODO 需要支持上线广播提醒吗？
        :return:
        '''
        sql = 'update user set isOnline = 1 where nickName = %s;'
        self.mysqlhelper.create_update_delete(sql,[self.nickname])

    def upline(self):
        pass

if __name__ == '__main__':
    r1 = SignIn('test','233')
    r1.singin()
