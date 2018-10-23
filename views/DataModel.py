from views.app import db


class User(db.Model):
    __tablename__ = 'ai_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    passwd = db.Column(db.String(255))

    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def __repr__(self):
        return '<User %r>' % self.name


# 服务表
class AIServer(db.Model):
    __tablename__ = 'ai_server'
    id = db.Column(db.Integer, primary_key=True)
    ip_id = db.Column(db.Integer)
    ip = db.Column(db.String(100))
    port = db.Column(db.String(100))
    server_addr = db.Column(db.String(100))
    server_type = db.Column(db.Integer)
    server_remark = db.Column(db.String(255))
    server_status = db.Column(db.Integer)
    create_time = db.Column(db.DATETIME)
    creator = db.Column(db.String(50))

    def __init__(self, ipId, ip, port, serverAddr, serverType, serverRemark, serverStatus, createTime, creator):
        self.ip_id = ipId
        self.ip = ip
        self.port = port
        self.server_addr = serverAddr
        self.server_type = serverType
        self.server_remark = serverRemark
        self.server_status = serverStatus
        self.create_time = createTime
        self.creator = creator


# ip 表
class Ip(db.Model):
    __tablename__ = 'ai_ip'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))
    remark = db.Column(db.String(255))
    create_time = db.Column(db.DateTime)
    creator = db.Column(db.String(100))

    def __init__(self, ip, remark, create_time, creator):
        self.ip = ip
        self.remark = remark
        self.create_time = create_time
        self.creator = creator

# top方法
class TM(object):
    def __init__(self, method, num, preTime, time):
        self.method = method
        self.num = num
        self.preTime = preTime
        self.time = time


# 黄页
class YellowPages(db.Model):
    __tablename__ = 'ai_yellow_pages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(255))
    type = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    creator = db.Column(db.String(100))

    def __init__(self, name, url, type, create_time, creator):
        self.name = name
        self.url = url
        self.type = type
        self.create_time = create_time
        self.creator = creator

