import flask
from flask import request
from www.sqlconfig import Ip, app, AIServer,scheduler,db
from www.serverReq import gethttp
import numpy as np
import datetime
from sshserver.config import paramikoclient
from sshserver.test1 import transportclient

client={}

@app.route('/',methods = ['GET','POST'])
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
    return flask.render_template('server.html',servers=servers,form = request.form)

@app.route('/addServer',methods=['POST'])
def addServer():
    form = request.form
    a = AIServer('1',form['ip'],form['port'],form['server_addr'],form['server_type'],form['server_remark'],0,datetime.datetime.now(),'sys')
    db.session.add(a)
    db.session.commit()
    return 'dataFromAjax'


# cmd
@app.route('/cmd',methods=['GET'])
def cmd():
    arg = request.args['arg']
    client_cmd = paramikoclient()
    alt = client_cmd.run_ssh(arg)
    client_cmd.close()
    return  alt
# 连接linux
@app.route('/connect1',methods=['GET'])
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
@app.route('/close',methods=['GET'])
def close():
    global client
    shell = client.get('172.17.34.4')
    shell.close()
    return 'success'

# shell
@app.route('/shell',methods=['GET'])
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



if __name__ == '__main__':
    app.debug=True
    scheduler.add_job(func=gethttp, id='1', args=(), trigger='interval', seconds=60, replace_existing=False)
    scheduler.init_app(app=app)
    scheduler.start()
    app.run()