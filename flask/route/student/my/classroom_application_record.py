from flask import Blueprint, request, json
from mysql import *


route_classroom_application_record = Blueprint(name="route_classroom_application_record", import_name=__name__)


# 学生端我的-申请记录-教室申请记录
@route_classroom_application_record.route('/classroom_application_record_load', methods=['POST'])
def classroom_application_record_load():
    resp = {'i': {}}
    username = int(json.loads(request.values.get("username")))
    res = Classroom.query.filter_by(school_number=username).all()
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


# 学生端我的-申请记录-教室申请记录-教室申请记录详细内容
@route_classroom_application_record.route('/classroom_application_record_detail', methods=['POST'])
def classroom_application_record_detail():
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
    information['check_method'] = res.check_method
    information['result'] = res.result
    return json.dumps(information)
