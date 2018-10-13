import flask
from flask import request
from www.sqlconfig import Ip, app, AIServer,scheduler
from www.serverReq import gethttp
import numpy as np


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


if __name__ == '__main__':
    app.debug=True
    scheduler.add_job(func=gethttp, id='1', args=(), trigger='interval', seconds=60, replace_existing=False)
    scheduler.init_app(app=app)
    scheduler.start()
    app.run()