from flask import Blueprint, request, json
from mysql import *


route_school_certificate_check_record = Blueprint(name="route_school_certificate_check_record", import_name=__name__)


# 教师端我的-审核记录-在学证明审核记录
@route_school_certificate_check_record.route('/school_certificate_check_record_load', methods=['POST'])
def school_certificate_check_record_load():
    resp = {'i': {}}
    college = str(json.loads(request.values.get("college")))
    res = SchoolCertificate.query.filter(SchoolCertificate.choose_college == college).all()
    information = []
    for i in res:
        i = {
            "sequence_number": str(i.sequence_number),
            "application_reason": str(i.application_reason),
            "submit_time": str(i.submit_time),
        }
        information.append(i)
    resp['i']['list'] = information
    return json.dumps(resp)


# 教师端我的-审核记录-在学证明审核记录-时间段查询
@route_school_certificate_check_record.route('/school_certificate_check_record_select', methods=['POST'])
def school_certificate_check_record_select():
    resp = {'i': {}}
    college = str(json.loads(request.values.get("college")))
    begin_date = str(json.loads(request.values.get("begin_date")))
    begin_time = str(json.loads(request.values.get("begin_time")))
    end_date = str(json.loads(request.values.get("end_date")))
    end_time = str(json.loads(request.values.get("end_time")))
    begin_datetime = begin_date + " " + begin_time
    end_datetime = end_date + " " + end_time
    res = db.engine.execute(
        "select sequence_number,application_reason,submit_time,check_method,result from school_certificate where choose_college=%s and submit_time BETWEEN %s AND %s",
        (college, begin_datetime, end_datetime))
    information = []
    for i in res:
        i = {
            "sequence_number": str(i.sequence_number),
            "application_reason": str(i.application_reason),
            "submit_time": str(i.submit_time),
        }
        information.append(i)
    resp['i']['list'] = information
    return json.dumps(resp)


# 教师端我的-审核记录-在学证明审核记录-在学证明审核记录详细内容
@route_school_certificate_check_record.route('/school_certificate_check_record_detail', methods=['POST'])
def school_certificate_check_record_detail():
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    information = {}
    res = SchoolCertificate.query.filter_by(sequence_number=sequence_number).first()
    information['name'] = res.name
    information['school_number'] = str(res.school_number)
    information['choose_college'] = res.choose_college
    information['profession'] = res.profession
    information['application_reason'] = res.application_reason
    information['submit_time'] = str(res.submit_time)
    information['check_method'] = res.check_method
    information['result'] = res.result
    return json.dumps(information)
