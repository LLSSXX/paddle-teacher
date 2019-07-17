from flask import Blueprint, request, json
from mysql import *


route_apply_activity = Blueprint(name="route_apply_activity", import_name=__name__)


# 学生端首页-申请活动
@route_apply_activity.route('/submit_activity_application', methods=['POST'])
def submit_activity_application():
    username = int(json.loads(request.values.get("username")))
    date_time = str(json.loads(request.values.get("date_time")))
    area = str(json.loads(request.values.get("area")))
    use_date = str(json.loads(request.values.get("date")))
    begin_time = str(json.loads(request.values.get("begin_time")))
    end_time = str(json.loads(request.values.get("end_time")))
    purpose = str(json.loads(request.values.get("purpose")))

    # 前端传回的地点信息为数字，需转换为相应地点名称
    if area == "1":
        str_area = "图书馆"
    if area == "2":
        str_area = "时间广场"
    if area == "3":
        str_area = "风雨操场"

    res = db.engine.execute(
        "select * from activity where area=%s and use_date=%s and ((begin_time BETWEEN %s AND %s) or (end_time BETWEEN %s AND %s)) ",
        (str_area, use_date, begin_time, end_time, begin_time, end_time))

    information = []
    for i in res:
        i = {
            "sequence_number": str(i.sequence_number)
        }
        information.append(i)
    print(information)

    if information == []:
        res1 = Login.query.filter_by(username=username).first()
        name = res1.name
        school_number = res1.username
        college = res1.college
        profession = res1.profession
        res2 = Activity(name=name, school_number=school_number, college=college, profession=profession,
                         area=str_area, use_date=use_date, begin_time=begin_time, end_time=end_time,
                         purpose=purpose, submit_time=date_time, check_method="人工审核", result="未审核", isuploading="未上传")
        db.session.add(res2)
        db.session.commit()
    else:
        return "已有人申请"

    return '申请活动'
