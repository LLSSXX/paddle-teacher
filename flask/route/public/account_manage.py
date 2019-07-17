from flask import Blueprint, request, json
from mysql import *
from werkzeug.security import generate_password_hash


route_account_manage = Blueprint(name="route_account_manage", import_name=__name__)


# 我的-账号管理-更改密码
@route_account_manage.route('/change_password', methods=['POST'])
def change_password():
    username = int(json.loads(request.values.get("username")))
    old_password = int(json.loads(request.values.get("old_password")))
    new_password = int(json.loads(request.values.get("new_password")))
    ensure_new_password = int(json.loads(request.values.get("ensure_new_password")))
    pw_hash = generate_password_hash(new_password)
    res = Login.query.filter_by(username=username).first()
    if res.password != old_password:
        return json.dumps(str("原密码错误！"))
    elif new_password != ensure_new_password:
        return '两次输入的新密码不一致，请重新输入！'
    else:
        db.engine.execute("update `login` set password = %s where username = %s", (pw_hash, username))
        return '更改密码成功，请重新登录'

    return '更改密码'


# 我的-账号管理-更改密保问题-页面加载时查找用户的密保问题
@route_account_manage.route('/change_question', methods=['GET'])
def change_question():
    username = int(json.loads(request.values.get("username")))
    res = SecurityQuestion.query.filter_by(username=username).first()
    question = res.question
    return json.dumps(question)


# 我的-账号管理-更改密保问题-点击确定后判断答案是否正确
@route_account_manage.route('/change_question/check_question', methods=['POST'])
def change_question_check_question():
    username = int(json.loads(request.values.get("username")))
    answer = str(json.loads(request.values.get("answer")))
    res = SecurityQuestion.query.filter_by(username=username).first()
    if res.answer != answer:
        return json.dumps(str("答案错误!"))
    else:
        return json.dumps(str("答案正确"))

    return "点击确定后判断答案是否正确"


# 我的-账号管理-更改密保问题-答案判断为正确后设置新密保问题
@route_account_manage.route('/change_question/set_new_question', methods=['POST'])
def change_question_set_new_question():
    username = int(json.loads(request.values.get("username")))
    choose_question = int(json.loads(request.values.get("choose_question")))
    answer = str(json.loads(request.values.get("answer")))
    if choose_question == 1:
        db.engine.execute("update `security_question` set question = '你最喜欢的颜色', answer = %s where username = %s",
                          (answer, username))
        return "更改密保问题成功"

    if choose_question == 2:
        db.engine.execute("update `security_question` set question = '你最喜欢的动物', answer = %s where username = %s",
                          (answer, username))
        return "更改密保问题成功"

    if choose_question == 3:
        db.engine.execute("update `security_question` set question = '你最喜欢的运动', answer = %s where username = %s",
                          (answer, username))
        return "更改密保问题成功"

    return '答案判断为正确后设置新密保问题'


# 我的-账号管理-更改密保答案-自动出现用户已设置的密保问题
@route_account_manage.route('/change_answer/select_question', methods=['GET'])
def change_answer_select_question():
    username = int(json.loads(request.values.get("username")))
    res = SecurityQuestion.query.filter_by(username=username).first()
    question = res.question
    return json.dumps(question)


# 我的-账号管理-更改密保答案-提交密保答案
@route_account_manage.route('/change_answer/submit_answer', methods=['POST'])
def change_answer_submit_answer():
    username = int(json.loads(request.values.get("username")))
    answer = str(json.loads(request.values.get("answer")))
    new_answer = str(json.loads(request.values.get("new_answer")))
    ensure_new_answer = str(json.loads(request.values.get("ensure_new_answer")))
    res = SecurityQuestion.query.filter_by(username=username).first()
    if res.answer != answer:
        return json.dumps(str("原答案错误！"))
    elif new_answer != ensure_new_answer:
        return '两次输入的新答案不一致，请重新输入！'
    else:
        db.engine.execute("update `security_question` set answer = %s where username = %s", (new_answer, username))
        return '更改密保答案成功'

    return '提交密保答案'

