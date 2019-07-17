from flask import Blueprint, request, json
from mysql import *


route_apply_classroom = Blueprint(name="route_apply_classroom", import_name=__name__)


# 学生端首页-申请教室
@route_apply_classroom.route('/submit_classroom_application', methods=['POST'])
def submit_classroom_application():
    username = int(json.loads(request.values.get("username")))
    date_time = str(json.loads(request.values.get("date_time")))
    classroom = json.loads(request.values.get("classroom"))
    use_date = str(json.loads(request.values.get("date")))
    begin_time = str(json.loads(request.values.get("begin_time")))
    end_time = str(json.loads(request.values.get("end_time")))
    purpose = str(json.loads(request.values.get("purpose")))

    # 前端传回的教室信息为数字，需转换为相应教室名称
    if classroom[0] == 1:
        if classroom[1] == 0:
            if classroom[2] == 0:
                str_classroom = "博理楼A区101"
            if classroom[2] == 1:
                str_classroom = "博理楼A区102"
            if classroom[2] == 2:
                str_classroom = "博理楼A区103"
            if classroom[2] == 3:
                str_classroom = "博理楼A区104"
        if classroom[1] == 1:
            if classroom[2] == 0:
                str_classroom = "博理楼B区111"
            if classroom[2] == 1:
                str_classroom = "博理楼B区112"
        if classroom[1] == 2:
            if classroom[2] == 0:
                str_classroom = "博理楼C区210"
            if classroom[2] == 1:
                str_classroom = "博理楼C区211"
            if classroom[2] == 2:
                str_classroom = "博理楼C区212"
        if classroom[1] == 3:
            if classroom[2] == 0:
                str_classroom = "博理楼D区220"
            if classroom[2] == 1:
                str_classroom = "博理楼D区221"
            if classroom[2] == 2:
                str_classroom = "博理楼D区222"
    if classroom[0] == 2:
        if classroom[1] == 0:
            if classroom[2] == 0:
                str_classroom = "劝学楼A区101"
            if classroom[2] == 1:
                str_classroom = "劝学楼A区102"
            if classroom[2] == 2:
                str_classroom = "劝学楼A区103"
            if classroom[2] == 3:
                str_classroom = "劝学楼A区104"
        if classroom[1] == 1:
            if classroom[2] == 0:
                str_classroom = "劝学楼B区111"
            if classroom[2] == 1:
                str_classroom = "劝学楼B区222"
        if classroom[1] == 2:
            if classroom[2] == 0:
                str_classroom = "劝学楼C区210"
            if classroom[2] == 1:
                str_classroom = "劝学楼C区211"
            if classroom[2] == 2:
                str_classroom = "劝学楼C区212"

    res = db.engine.execute(
        "select * from classroom where classroom=%s and use_date=%s and ((begin_time BETWEEN %s AND %s) or (end_time BETWEEN %s AND %s)) ",
        (str_classroom, use_date, begin_time, end_time, begin_time, end_time))

    information = []
    for i in res:
        i = {
            "sequence_number": str(i.sequence_number)
        }
        information.append(i)

    if information == []:
        res1 = Login.query.filter_by(username=username).first()
        name = res1.name
        school_number = res1.username
        college = res1.college
        profession = res1.profession
        res2 = Classroom(name=name, school_number=school_number, college=college, profession=profession,
                         classroom=str_classroom, use_date=use_date, begin_time=begin_time, end_time=end_time,
                         purpose=purpose, submit_time=date_time, check_method="人工审核", result="未审核", isuploading="未上传")
        db.session.add(res2)
        db.session.commit()
    else:
        return "已有人申请"

    return '申请教室'
