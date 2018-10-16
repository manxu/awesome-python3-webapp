import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.17.34.4',port=22,username='root',password='dev_201704')
while True:
    input_command = input('>>>=')
    if input_command == 'quit':
        break
    stdin,stdout,stderr = ssh.exec_command(input_command, get_pty=True)
    result = stdout.read()
    if len(result) == 0:
        print(stderr.read())
    else:
        print(str(result,'utf-8'))
ssh.close()

if __name__ == '__main__':
    pass