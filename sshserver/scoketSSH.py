import paramiko
import re
from time import *


# linux长连接方式类似xshell
class transportclient(object):
    def __init__(self, ip, port, username, password, timeout=30):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout
        self.transport = ''
        self.chan = ''
        self.try_times = 3

    # 连接远程主机
    def connect(self):
        while True:
            try:
                self.transport = paramiko.Transport(sock=(self.ip, self.port))
                self.transport.connect(username=self.username, password=self.password)
                self.chan = self.transport.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                # 如果没有抛出异常说明连接成功，直接返回
                print(u'连接%s成功' % self.ip)
                sleep(0.5)
                # 接收到的网络数据解码为str
                str = self.chan.recv(65535).decode('utf-8')
                return True,str
            except Exception as e1:
                if self.try_times != 0:
                    print(u'连接%s失败，进行重试' % self.ip)
                    self.try_times -= 1
                else:
                    print(u'重试3次失败，结束程序')
                    exit(1)
            return False,'连接失败'

    # 断开连接
    def close(self):
        self.chan.close()
        self.transport.close()

    def send(self, cmd):
        # 通过命令执行提示符来判断命令是否执行完成
        p = re.compile('root@scdel-02:.*?#')
        result = ''
        # 发送要执行的命令
        self.chan.send(cmd + '\r')
        sleep(0.5)
        ret = self.chan.recv(65535)
        ret = ret.decode('utf-8')
        result += ret
        str = re.compile('(\\x1b\[[0-9]*;[0-9]*m)|(\\x1b\[[0-9]?m)')
        b = str.sub('',result)
        return b


# 连接正常的情况
if __name__ == '__main__':
    host = transportclient('172.17.34.4',22, 'root', 'dev_201704') #传入Ip，用户名，密码
    host.connect()
    while True:
        input_command = input()
        if input_command=='quit':
            break
        result=host.send(input_command) #发送一个查看ip的命令
        print(result)
    host.close()