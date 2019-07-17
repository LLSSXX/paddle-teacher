from flask import Blueprint, request, json
from mysql import *


route_check_school_certificate = Blueprint(name="route_check_school_certificate", import_name=__name__)


# 教师端首页-审核在学证明-待审核在学证明
@route_check_school_certificate.route('/wait_check_school_certificate', methods=['POST'])
def wait_check_school_certificate():
    resp = {'i': {}}
    college = str(json.loads(request.values.get("college")))
    res = SchoolCertificate.query.filter(SchoolCertificate.choose_college == college,
                                         SchoolCertificate.result == "未审核").all()
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


# 教师端首页-审核在学证明-待审核在学证明-待审核在学证明详细内容
@route_check_school_certificate.route('/wait_check_school_certificate/wait_check_school_certificate_detail', methods=['POST'])
def wait_check_school_certificate_detail():
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    information = {}
    res = SchoolCertificate.query.filter_by(sequence_number=sequence_number).first()
    information['name'] = res.name
    information['school_number'] = str(res.school_number)
    information['choose_college'] = res.choose_college
    information['profession'] = res.profession
    information['application_reason'] = res.application_reason
    information['submit_time'] = str(res.submit_time)
    return json.dumps(information)


# 教师端首页-审核在学证明-待上传在学证明
@route_check_school_certificate.route('/wait_upload_school_certificate', methods=['POST'])
def wait_upload_school_certificate():
    resp = {'i': {}}
    college = str(json.loads(request.values.get("college")))
    res = SchoolCertificate.query.filter(SchoolCertificate.choose_college == college,
                                         SchoolCertificate.result != "未审核",
                                         SchoolCertificate.isuploading == "未上传").all()
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


# 教师端首页-审核在学证明-待上传在学证明-上传
@route_check_school_certificate.route('/wait_upload_school_certificate/wait_upload_school_certificate_upload', methods=['POST'])
def wait_upload_school_certificate_upload():
    college = str(json.loads(request.values.get("college")))
    db.engine.execute(
        "update `school_certificate` set isuploading = '已上传' where choose_college = %s and isuploading = '未上传' and result not in ('未审核')",
        (college))

    return "上传"


# 教师端首页-审核在学证明-待上传在学证明-待上传在学证明详细内容
@route_check_school_certificate.route('/wait_upload_school_certificate/wait_upload_school_certificate_detail', methods=['POST'])
def wait_upload_school_certificate_detail():
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    information = {}
    res = SchoolCertificate.query.filter_by(sequence_number=sequence_number).first()
    information['name'] = res.name
    information['school_number'] = str(res.school_number)
    information['choose_college'] = res.choose_college
    information['profession'] = res.profession
    information['application_reason'] = res.application_reason
    information['submit_time'] = str(res.submit_time)
    return json.dumps(information)


# 教师端首页-审核在学证明-通过
@route_check_school_certificate.route('/check_school_certificate_choose_pass', methods=['POST'])
def check_school_certificate_choose_pass():
    username = int(json.loads(request.values.get("username")))
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    res = Login.query.filter_by(username=username).first()
    check_people_name = res.name
    db.engine.execute(
        "update `school_certificate` set result = '通过', check_people_name = %s, check_people_number = %s where sequence_number = %s",
        (check_people_name, username, sequence_number))

    return "判断通过"


# 教师端首页-审核在学证明-不通过
@route_check_school_certificate.route('/check_school_certificate_choose_dispass', methods=['POST'])
def check_school_certificate_choose_dispass():
    username = int(json.loads(request.values.get("username")))
    sequence_number = int(json.loads(request.values.get("sequence_number")))
    res = Login.query.filter_by(username=username).first()
    check_people_name = res.name
    db.engine.execute(
        "update `school_certificate` set result = '不通过', check_people_name = %s, check_people_number = %s where sequence_number = %s",
        (check_people_name, username, sequence_number))

    return "判断不通过"