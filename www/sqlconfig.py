from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.99.100/activiti_api'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 数据库
db = SQLAlchemy(app)
#定时任务
scheduler = APScheduler()

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