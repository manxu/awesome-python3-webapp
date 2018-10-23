import configparser,paramiko


# ssh连接参数
class paramikoclient(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('sshserver/config.ini')
        self.host = self.config.get('ssh', 'host')
        self.port = self.config.get('ssh', 'port')
        self.user = self.config.get('ssh', 'user')
        self.pwd = self.config.get('ssh', 'pwd')
        self.timeout = self.config.get('ssh', 'timeout')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.host,port=self.port,username=self.user,password=self.pwd,timeout=float(self.timeout))

    def run_ssh(self,cmd_command):
        stdin,stdout,stderr = self.client.exec_command(cmd_command)
        result = stdout.read()  # read方法读取输出结果
        if len(result) == 0:  # 判断如果输出结果长度等于0表示为错误输出
            return stderr.read().decode()
        else:
            return str(result, 'utf-8')

    def close(self):
        self.client.close()


if __name__ == '__main__':
    client_cmd = paramikoclient('config.ini')
    while True:
        cmd_input=input('>>>:')
        client_cmd.run_ssh(cmd_input)
        if cmd_input == 'quit':
            client_cmd.close()