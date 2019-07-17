from flask import Blueprint, request, json
from mysql import *


route_my = Blueprint(name="route_my", import_name=__name__)


# 我的-显示用户姓名和学号
@route_my.route('/my', methods=['GET'])
def my():
    username = int(json.loads(request.values.get("username")))
    res = Login.query.filter_by(username=username).first()
    name = res.name
    return json.dumps(name)

