from flask import request,render_template,Blueprint
from views.DataModel import Ip, AIServer,TM
import numpy as np
import datetime
from sshserver.ssh import paramikoclient
from sshserver.scoketSSH import transportclient

admin = Blueprint('admin', __name__)    # url_prefix='/'


client={}

@admin.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        filters = []
        if request.values.get('ip')!='':
            filters.append(AIServer.ip==request.values.get('ip'))
        if request.values.get('port')!='':
            filters.append(AIServer.port == request.values.get('port'))
        if request.values.get('server_type')!='':
            filters.append(AIServer.server_type == request.values.get('server_type'))
        if request.values.get('server_addr')!='':
            filters.append(AIServer.server_addr == request.values.get('server_addr'))
        f = np.array(filters)
        servers = AIServer.query.filter(*f).order_by("server_status").all()
    else:
        servers = AIServer.query.order_by("server_status").all()
    return render_template('server.html',servers=servers,form = request.form)

@admin.route('/addServer',methods=['POST'])
def addServer():
    form = request.form
    a = AIServer('1',form['ip'],form['port'],form['server_addr'],form['server_type'],form['server_remark'],0,datetime.datetime.now(),'sys')
    db.session.add(a)
    db.session.commit()
    return 'dataFromAjax'


# cmd
@admin.route('/cmd',methods=['GET'])
def cmd():
    arg = request.args['arg']
    client_cmd = paramikoclient()
    alt = client_cmd.run_ssh(arg)
    client_cmd.close()
    return  alt
# 连接linux
@admin.route('/connect1',methods=['GET'])
def connect1():
    global client
    shell = client.get('172.17.34.4')
    if shell==None:
        shell = transportclient('172.17.34.4',22, 'root', 'dev_201704')
        client['172.17.34.4'] = shell
    x,y = shell.connect()
    if not x:
        return '连接失败'
    return y

# 连接linux
@admin.route('/close',methods=['GET'])
def close():
    global client
    shell = client.get('172.17.34.4')
    shell.close()
    return 'success'

# shell
@admin.route('/shell',methods=['GET'])
def shell():
    arg = request.args['arg']
    global client
    shell = client.get('172.17.34.4')
    if shell==None:
        shell = transportclient('172.17.34.4',22, 'root', 'dev_201704')
        if not shell.connect():
            return '连接失败'
        client['172.17.34.4'] = shell
    alt = shell.send(arg)
    # shell.close()
    return  alt

# top方法
@admin.route('/topMethod',methods=['GET','POST'])
def topMethod():
    p = None
    if request.method == 'POST':
        p = request.form['method']
    miko = paramikoclient()
    sftp_client = miko.client.open_sftp()
    remote_file = sftp_client.open("/root/logs/topmethod.log")#文件路径
    topMethods = []
    try:
        for line in remote_file:
            s = line.split('\t')
            tm = TM(s[0],s[1],s[2],s[3])
            if p:
                if p in tm.method:
                    topMethods.append(tm)
            else:
                topMethods.append(tm)
    except Exception as e:
        print(e)
    finally:
        remote_file.close()
    return render_template('topmethod.html',topMethods=topMethods,form = request.form)

