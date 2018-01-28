import sys
sys.path.append('H:\Project\PythonChat')
from share.sha import getSha1
import json

class SignIn():

    def __init__(self,udp_socket,addr):
        self.udp_socket = udp_socket
        self.addr = addr

    def show_start_GUI(self):
        print('注册-输入:1'.center(40))
        print('登录-输入:2'.center(40))
        num = input('输入数字:')
        if num == '1':
            self.register()
        elif num == '2':
            return self.signin()
        else:
            print('输入不合法！')

    def signin(self):
        self._get_nickname_password()
        data = {'event':'signin'
                ,'nickname':self.nickname
                ,'password':self.password}
        data1 = json.dumps(data)
        self.udp_socket.sendto(data1.encode(),self.addr)
        result = self.udp_socket.recvfrom(1024)
        res = result[0].decode()
        print(res)
        if res == '登录成功':
            return True

    def register(self):
        self._get_nickname_password()
        data = {'event':'register'
                ,'nickname':self.nickname
                ,'password':self.password}
        data1 = json.dumps(data)
        self.udp_socket.sendto(data1.encode(),self.addr)
        result = self.udp_socket.recvfrom(1024)
        print(result[0].decode())
        return True

    def _get_nickname_password(self):
        self.nickname = input('请输入昵称:')
        password = self._get_password1('请输入密码: ') # TODO 优化密码输入
        sys.path.append('..')
        self.password = getSha1(password)

    def _get_password(self,prompt): # 会以*提示输入
        import msvcrt
        count = 0
        chars = []
        print(prompt)
        while True:
            new_char = msvcrt.getch()
            if new_char in b'\r\n':
                break
            elif new_char == b'\0x3':  # ctrl + c
                raise KeyboardInterrupt
            elif new_char == b'\b':
                if chars and count >= 0:
                    count -= 1
                    chars = chars[:-1]
                    msvcrt.putch(b'\b')
                    msvcrt.putch(b'\x20')  # space
                    msvcrt.putch(b'\b')
            else:
                if count < 0:
                    count = 0
                count += 1
                chars.append(new_char.decode('utf8'))
                msvcrt.putch(b'*')
        return ''.join(chars)
    def _get_password1(self,prompt): # 不提示输入个数
        import getpass
        return getpass.getpass('请输入密码：')


    def getUserNickName(self):
        return self.nickname
if __name__ == '__main__':
    s1 = SignIn(' ')
    s1.show_start_GUI()