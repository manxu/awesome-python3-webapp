from flask import Blueprint, render_template
from .DataModel import YellowPages

yellow = Blueprint('yellow', __name__)    # url_prefix='/'


# 网站
@yellow.route('/yellowPage', methods=['GET'])
def yellowPage():
    servers = YellowPages.query.order_by("type").all()
    websites = {}
    t1 = []
    t2 = []
    t3 = []
    websites['t1'] = t1
    websites['t2'] = t2
    websites['t3'] = t3
    for s in servers:
        website = {'id': s.id, 'name': s.name, 'url': s.url}
        websites['t' + str(s.type)].append(website)
    return render_template('yellowPages.html', websites=websites)

