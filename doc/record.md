# CS开发中，client使用字符界面开发与图形化界面开发的区别：
1. 图形化界面开发让用户容易理解这个产品的逻辑

# Client处理通信的线程在什么地方使用？
Client处理通信的线程功能是：
1. 解释server发送的消息，此操作会导致阻塞

可以选择的地方：
1. 主界面打开一个通信GUI时
    优点：
    缺点：
2. 在通信GUI中打开
    优点：
    缺点：

具体使用方法：
1. 新建一个继承自QThread的类
2. 在通信GUI中新建该类的实例
2. 调用该实例的start方法

# 反思的地方
1. 实现某个功能的几行代码有时不知道重构为一个函数
2. socket发送udp信息时，要确保addr有效（ip主机的port端口已打开）

# 遇到的错误
1. ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
原因：
1. socket在使用之前已经关闭了
2. addr不可用

