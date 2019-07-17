from flask import Blueprint, request, json
from mysql import *


route_activity_check_record = Blueprint(name="route_activity_check_record", import_name=__name__)


# 教师端我的-审核记录-活动审核记录
@route_activity_check_record.route('/activity_check_record_load', methods=['POST'])
def activity_check_record_load():
    resp = {'i': {}}
    college = str(json.loads(request.values.get("college")))
    res = Activity.query.filter(Activity.college == college).all()
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


# 教师端我的-审核记录-活动审核记录-查询
@route_activity_check_record.route('/activity_check_record_select', methods=['POST'])
def activity_check_record_select():
    resp = {'i': {}}
    college = str(json.loads(request.values.get("college")))
    begin_date = str(json.loads(request.values.get("begin_date")))
    begin_time = str(json.loads(request.values.get("begin_time")))
    end_date = str(json.loads(request.values.get("end_date")))
    end_time = str(json.loads(request.values.get("end_time")))
    begin_datetime = begin_date + " " + begin_time
    end_datetime = end_date + " " + end_time
    res = db.engine.execute(
        "select sequence_number,purpose,submit_time,check_method,result from activity where college=%s and submit_time BETWEEN %s AND %s",
        (college, begin_datetime, end_datetime))
    print(res)
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


# 教师端我的-审核记录-活动审核记录-活动审核记录详细内容
@route_activity_check_record.route('/activity_check_record_detail', methods=['POST'])
def activity_check_record_detail():
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    information = {}
    res = Activity.query.filter_by(sequence_number=sequence_number).first()
    information['name'] = res.name
    information['school_number'] = str(res.school_number)
    information['college'] = res.college
    information['profession'] = res.profession
    information['area'] = res.area
    information['use_date'] = str(res.use_date)
    information['begin_time'] = str(res.begin_time)
    information['end_time'] = str(res.end_time)
    information['purpose'] = res.purpose
    information['submit_time'] = str(res.submit_time)
    information['check_method'] = res.check_method
    information['result'] = res.result
    return json.dumps(information)

