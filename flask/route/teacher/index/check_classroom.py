from flask import Blueprint, request, json
from mysql import *


route_check_classroom = Blueprint(name="route_check_classroom", import_name=__name__)


# 教师端首页-审核教室-待审核教室
@route_check_classroom.route('/wait_check_classroom', methods=['POST'])
def wait_check_classroom():
    resp = {'i': {}}
    college = str(json.loads(request.values.get("college")))
    res = Classroom.query.filter(Classroom.college == college,
                                 Classroom.result == "未审核").all()
    information = []
    for i in res:
        i = {
            "sequence_number": str(i.sequence_number),
            "purpose": str(i.purpose),
            "use_date": str(i.use_date),
            "begin_time": str(i.begin_time),
            "end_time": str(i.end_time),
        }
        information.append(i)
    resp['i']['list'] = information
    return json.dumps(resp)


 # 教师端首页-审核教室-待审核教室-待审核教室详细内容
@route_check_classroom.route('/wait_check_classroom/wait_check_classroom_detail', methods=['POST'])
def wait_check_classroom_detail():
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    information = {}
    res = Classroom.query.filter_by(sequence_number=sequence_number).first()
    information['name'] = res.name
    information['school_number'] = str(res.school_number)
    information['college'] = res.college
    information['profession'] = res.profession
    information['classroom'] = res.classroom
    information['use_date'] = str(res.use_date)
    information['begin_time'] = str(res.begin_time)
    information['end_time'] = str(res.end_time)
    information['purpose'] = res.purpose
    information['submit_time'] = str(res.submit_time)
    return json.dumps(information)


# 教师端首页-审核教室-待上传教室
@route_check_classroom.route('/wait_upload_classroom', methods=['POST'])
def wait_upload_classroom():
    resp = {'i': {}}
    college = str(json.loads(request.values.get("college")))
    res = Classroom.query.filter(Classroom.college == college,
                                 Classroom.result != "未审核",
                                 Classroom.isuploading == "未上传").all()
    information = []
    for i in res:
        i = {
            "sequence_number": str(i.sequence_number),
            "purpose": str(i.purpose),
            "use_date": str(i.use_date),
            "begin_time": str(i.begin_time),
            "end_time": str(i.end_time),
        }
        information.append(i)
    resp['i']['list'] = information
    return json.dumps(resp)


# 教师端首页-审核教室-待审核教室-上传
@route_check_classroom.route('/wait_upload_classroom/wait_upload_classroom_upload', methods=['POST'])
def wait_upload_classroom_upload():
    college = str(json.loads(request.values.get("college")))
    db.engine.execute(
        "update `classroom` set isuploading = '已上传' where college = %s and isuploading = '未上传' and result not in ('未审核')",
        (college))

    return "上传"


# 教师端首页-审核教室-待上传教室-待上传教室详细内容
@route_check_classroom.route('/wait_upload_classroom/wait_upload_classroom_detail', methods=['POST'])
def wait_upload_classroom_detail():
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    information = {}
    res = Classroom.query.filter_by(sequence_number=sequence_number).first()
    information['name'] = res.name
    information['school_number'] = str(res.school_number)
    information['college'] = res.college
    information['profession'] = res.profession
    information['classroom'] = res.classroom
    information['use_date'] = str(res.use_date)
    information['begin_time'] = str(res.begin_time)
    information['end_time'] = str(res.end_time)
    information['purpose'] = res.purpose
    information['submit_time'] = str(res.submit_time)
    return json.dumps(information)


# 教师端首页-审核教室-通过
@route_check_classroom.route('/check_classroom_choose_pass', methods=['POST'])
def check_classroom_choose_pass():
    username = int(json.loads(request.values.get("username")))
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    res = Login.query.filter_by(username=username).first()
    check_people_name = res.name
    db.engine.execute(
        "update `classroom` set result = '通过', check_people_name = %s, check_people_number = %s where sequence_number = %s",
        (check_people_name, username, sequence_number))

    return "判断通过"


# 教师端首页-审核教室-不通过
@route_check_classroom.route('/check_classroom_choose_dispass', methods=['POST'])
def check_classroom_choose_dispass():
    username = int(json.loads(request.values.get("username")))
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    res = Login.query.filter_by(username=username).first()
    check_people_name = res.name
    db.engine.execute(
        "update `classroom` set result = '不通过', check_people_name = %s, check_people_number = %s where sequence_number = %s",
        (check_people_name, username, sequence_number))

    return "判断不通过"
