# 名称：局域网通信工具

# 使用场景：**企业局域网内办公**

# 简介
1. 项目采用CS模式，基于UDP传输用户消息，使用PyQt5开发GUI
2. client用户可以私聊、组聊、广播

## server：
1. 有两个线程。一个负责接收client数据，一个负责处理client请求
2. 使用MYSQL数据库保存用户注册信息

## client：
1. 有两个线程。一个负责程序主界面的事件循环，一个负责处理server的响应

# 功能
1. 用户注册
2. 用户登录验证
3. 用户密码加密保存
2. 向指定用户发送私密消息
2. 向指定用户组发送组消息
3. 向所有用户发送广播
4. 显示所有用户的状态，并统计用户状态（在线人数，离线人数）
5. 显示'关于'
1. 查看与所有用户和组通讯的历史消息
1. 查看、修改用户的信息

# 该项目开发环境
1. 开发语言：Python3
2. 编辑器：PyCharm
3. 主要程序库：PyQt5
4. OS：Windows10（由于Python的跨平台特性，可以在Linux下运行，可能需要一些小的改动）

# 环境搭建（针对Windows10，Linux类似）
1. 安装virtualenv
2. 新建一个Python3作为解释器的虚拟环境
3. 在该项目目录，且启动相应虚拟环境的条件下执行`pip install -r requirements.txt`就安装好开发环境了
3. 安装MySQL
3. DOS执行数据库导入（没有进入MySQL命令行界面），可安装数据库可视化软件方便数据库操作
```
导出数据库：
mysqldump -h HOSTNAME -uUSERNAME -p DBNAME > exported_db.sql
导入数据库：
mysql -h HOSTNAME -uUSERNAME -p DBNAME < exported_db.sql
```


# Python技术关键词
**网络编程**、**UDP**、**数据库**、**MYSQL**、**面向对象**、**PyQt5**、**设计模式**
