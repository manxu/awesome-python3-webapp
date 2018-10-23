from views.app import app,scheduler
from views.serverTask import gethttp
from views.server import admin
from views.yellowPages import yellow


app.register_blueprint(admin, url_prefix='/',template_folder='/templates')
app.register_blueprint(yellow, url_prefix='/',template_folder='/templates')

if __name__ == '__main__':
    app.debug = True
    scheduler.add_job(func=gethttp, id='1', args=(), trigger='interval', seconds=60, replace_existing=False)
    scheduler.init_app(app=app)
    scheduler.start()
    app.run()