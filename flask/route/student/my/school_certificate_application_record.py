from flask import Blueprint, request, json
from mysql import *


route_school_certificate_application_record = Blueprint(name="route_school_certificate_application_record", import_name=__name__)


# 学生端我的-申请记录-在学证明申请记录
@route_school_certificate_application_record.route('/school_certificate_application_record_load', methods=['POST'])
def school_certificate_application_record_load():
    resp = {'i': {}}
    username = int(json.loads(request.values.get("username")))
    res = SchoolCertificate.query.filter_by(school_number=username).all()
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


# 学生端我的-申请记录-在学证明申请记录-在学证明申请记录详细内容
@route_school_certificate_application_record.route('/school_certificate_application_record_detail', methods=['POST'])
def school_certificate_application_record_detail():
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