from flask import Blueprint, request, json
from mysql import *
from werkzeug.security import generate_password_hash, check_password_hash


route_login = Blueprint(name="route_login", import_name=__name__)


# 登录
@route_login.route('/login', methods=['POST'])
def login():
    username = int(json.loads(request.values.get("username")))
    password = str(json.loads(request.values.get("password")))
    res = Login.query.filter_by(username=username).first()
    result = SecurityQuestion.query.filter_by(username=username).first()
    if not res:
        return json.dumps(str("用户名或密码错误!"))
    if res:
        check_password = check_password_hash(res.password, password)
        if check_password == False:
            return json.dumps(str("用户名或密码错误!"))
        if not result:
            return json.dumps(str("需设置密保问题"))
        if result:
            if res.identity == "学生":
                return json.dumps(res.identity)
            if res.identity == "教师":
                information = {}
                information["identity"] = res.identity
                information["college"] = res.college
                return json.dumps(information)

    return '登录'


# 首次登录设置密保问题
@route_login.route('/first_login_set_question', methods=['POST'])
def first_login_set_question():
    username = int(json.loads(request.values.get("username")))
    choose_question = int(json.loads(request.values.get("choose_question")))
    answer = str(json.loads(request.values.get("answer")))
    r = Login.query.filter_by(username=username).first()
    if choose_question == 1:
        choose_question = "你最喜欢的颜色"
        res = SecurityQuestion(username=username, question=choose_question, answer=answer)
        db.session.add(res)
        db.session.commit()
        return json.dumps(r.identity)
    if choose_question == 2:
        choose_question = "你最喜欢的动物"
        res = SecurityQuestion(username=username, question=choose_question, answer=answer)
        db.session.add(res)
        db.session.commit()
        return json.dumps(r.identity)
    if choose_question == 3:
        choose_question = "你最喜欢的运动"
        res = SecurityQuestion(username=username, question=choose_question, answer=answer)
        db.session.add(res)
        db.session.commit()
        return json.dumps(r.identity)

    return '首次登录设置密保问题'


# 登录-忘记密码-自动出现用户已设置的密保问题
@route_login.route('/forget_password/select_question', methods=['GET'])
def forget_password_select_question():
    username = int(json.loads(request.values.get("username")))
    res = SecurityQuestion.query.filter_by(username=username).first()
    question = res.question
    return json.dumps(question)


# 登录-忘记密码-自动出现用户已设置的密保问题-用户输入密保问题的答案
@route_login.route('/forget_password/check_answer', methods=['POST'])
def forget_password_check_answer():
    username = int(json.loads(request.values.get("username")))
    answer = str(json.loads(request.values.get("answer")))
    res = SecurityQuestion.query.filter_by(username=username).first()
    if res.answer != answer:
        return json.dumps(str("答案错误"))
    else:
        return json.dumps(str("答案正确"))

    return '用户输入密保问题的答案'


# 登录-忘记密码-自动出现用户已设置的密保问题-用户输入密保问题的答案-设置新的密码
@route_login.route('/forget_password/set_new_password', methods=['POST'])
def forget_password_set_new_password():
    username = int(json.loads(request.values.get("username")))
    new_password = int(json.loads(request.values.get("new_password")))
    ensure_new_password = int(json.loads(request.values.get("ensure_new_password")))
    pw_hash = generate_password_hash(new_password)
    if new_password != ensure_new_password:
        return '两次输入的新密码不一致，请重新输入！'
    else:
        db.engine.execute("update `login` set password = %s where username = %s", (pw_hash, username))
        return '更改密码成功，请重新登录'

    return '设置新的密码'
