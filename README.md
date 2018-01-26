# 名称：局域网通信工具

# 使用场景：**企业局域网内办公**

# 简介：
1. 项目采用CS模式，基于UDP传输用户消息，字符界面显示信息
2. client用户之间可以收发消息
3. 若干client用户可以组为一组实现组内收发消息
4. client用户还可以向所有用户发送消息，即广播
5. client用户可以分享各自电脑屏幕，且可以定制分享区域
6. 设置了管理员，每个client账户由管理员分配
7. 管理员可以查看所有用户的通讯记录

# 功能

## client用户功能
1. 查看帮助
2. 发送组消息
3. 发送私聊消息
5. 查看在线用户数量及名字
6. 查看聊天历史
7. 查看组聊天历史
8. 可以增删改查、本人信息
9. 查看其他用户信息
10. 查看本人所在组
11. 查看组长
13. 向好友发送文件
14. 执行系统命令
15. client用户可以分享各自电脑屏幕，且可以定制分享区域

## 管理员功能
具有用户的所有功能，还具有：
1. 分配用户账号
2. 查看client用户消息
3. 查看client通讯记录

# 开发环境
1. 开发语言：Python3
2. 编辑器：PyCharm

# 开发计划

## 第1阶段：实现基础功能（先用最'笨'，最'老实'的方法）：
计划使用7天的时间实现基础功能。
使用面向对象的思想来编程，比如：
1. 在client新建一个Worker类实现业务逻辑
2. 在server新建一个Worker类实现业务逻辑，管理数据库的类Db

### server实现：
1. 有两个线程。一个负责接收终端输入，一个负责处理client发连接处理
2. 使用MYSQL数据库保存用户注册信息
3. 用户登录验证（登录信息与服务器）
4. 数据库表的设计

### client实现：
1. 主进程新建两个子线程来分别处理用户输入的数据和用户接收服务器的数据 

## 第2阶段：添加新功能及程序性能优化
1. 使用高性能网络框架（因为业务逻辑没变，变的只是框架，重构应该不是十分复杂）
2. 使用PyQt开发GUI界面
3. 使用ORM技术（sqlalchemy）来管理数据库
4. 实现屏幕共享功能
5. 使用FTP协议传输小文本文件

# Python技术关键词
**网络编程**、**UDP**、**数据库**、**MYSQL**、**面向对象**、**PyQt5**、**设计模式**