from flask import Blueprint, request, json
from mysql import *
from text_model.u_model import use_model


route_apply_school_certificate = Blueprint(name="route_apply_school_certificate", import_name=__name__)


# 学生端首页-申请在学证明-页面加载时自动查询用户基本信息
@route_apply_school_certificate.route("/school_certificate_load", methods=['GET'])
def school_certificate_load():
    # 从前端获取用户名
    username = int(json.loads(request.values.get("username")))
    # 在数据库login表中查询该用户的基本信息
    res = Login.query.filter_by(username=username).first()
    # 将数据库中查询到的数据存入information中
    information = {}
    information['name'] = res.name
    information['school_number'] = str(res.username)
    information['college'] = res.college
    information['profession'] = res.profession
    # 将infomation传回前端
    return json.dumps(information)


# 学生端首页-申请在学证明-预览
@route_apply_school_certificate.route('/preview', methods=['POST'])
def preview():
    username = int(json.loads(request.values.get("username")))
    res = Login.query.filter_by(username=username).first()
    information = {}
    information['name'] = res.name
    information['school_number'] = str(res.username)
    information['college'] = res.college
    information['profession'] = res.profession
    information['grade'] = res.grade
    return json.dumps(information)


# 学生端首页-申请在学证明-提交在学证明
@route_apply_school_certificate.route('/submit_school_certificate_application', methods=['POST'])
def submit_school_certificate_application():
    username = int(json.loads(request.values.get("username")))
    application_reason = str(json.loads(request.values.get("application_reason")))
    date_time = str(json.loads(request.values.get("date_time")))
    res = Login.query.filter_by(username=username).first()

    # 使用模型给申请理由打标签
    judgement = use_model(application_reason)

    # 根据标签向数据库的school_certificate表中存入对应的数据
    if judgement == "pass":
        res = SchoolCertificate(name=res.name, school_number=res.username, choose_college=res.college,
                                profession=res.profession,
                                application_reason=application_reason, check_method="自动审核", result="通过",
                                submit_time=date_time)
        db.session.add(res)
        db.session.commit()
        return "Pass"
    elif judgement == "undetermined":
        res = SchoolCertificate(name=res.name, school_number=res.username, choose_college=res.college,
                                profession=res.profession,
                                application_reason=application_reason, check_method="人工审核", result="未审核",
                                isuploading="未上传", submit_time=date_time)
        db.session.add(res)
        db.session.commit()
        return "Undetermined"
    elif judgement == "fail":
        res = SchoolCertificate(name=res.name, school_number=res.username, choose_college=res.college,
                                profession=res.profession,
                                application_reason=application_reason, check_method="自动审核", result="未通过",
                                submit_time=date_time)
        db.session.add(res)
        db.session.commit()
        return "Dispass"
    else:
        return "error"

    return '提交在学证明'


