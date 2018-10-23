# from .app import admin
# from .yellowPages import yellow
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_apscheduler import APScheduler
# from .serverReq import gethttp
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.99.100/activiti_api'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# # 数据库
# db = SQLAlchemy(app)
# #定时任务
# scheduler = APScheduler()
# app.register_blueprint(admin)
# app.register_blueprint(yellow)
#
#
