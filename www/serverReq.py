from urllib import request
from www.sqlconfig import AIServer
from www.sqlconfig import db


def gethttp():
    user = AIServer.query.all()
    for u in user:
        serverId = u.id
        apiServer = AIServer.query.filter_by(id=serverId).first()
        url = 'http://'+apiServer.ip + ":" + apiServer.port + apiServer.server_addr
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        try:
            f = request.urlopen(req)
            print('Status:', f.status, f.reason)
            if f.status == 200:
                apiServer.server_status = 1
            else:
                apiServer.server_status = 0
            db.session.add(apiServer)
            db.session.commit()
        except BaseException:
            apiServer.server_status = 0
            db.session.add(apiServer)
            db.session.commit()

if __name__ == '__main__':
    gethttp(1)