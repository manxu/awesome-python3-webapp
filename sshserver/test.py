#!/usr/bin/env python
#coding:utf8
import paramiko
#实例化一个transport对象
transport = paramiko.Transport(('192.168.99.100',22))
#建立连接
transport.connect(username='docker',password='tcuser')
#建立ssh对象
ssh = paramiko.SSHClient()
#绑定transport到ssh对象
ssh._transport=transport
#执行命令
stdin,stdout,stderr=ssh.exec_command('df')
#打印输出
print(stdout.read().decode())
#关闭连接
transport.close()