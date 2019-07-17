# -*- coding: utf-8 -*-
from flask import Flask
from mysql import *
from route.student.index.apply_school_certificate import route_apply_school_certificate
from route.student.index.apply_classroom import route_apply_classroom
from route.student.index.apply_activity import route_apply_activity
from route.student.my.school_certificate_application_record import route_school_certificate_application_record
from route.student.my.classroom_application_record import route_classroom_application_record
from route.student.my.activity_application_record import route_activity_application_record
from route.teacher.index.check_school_certificate import route_check_school_certificate
from route.teacher.index.check_classroom import route_check_classroom
from route.teacher.index.check_activity import route_check_activity
from route.teacher.my.school_certificate_check_record import route_school_certificate_check_record
from route.teacher.my.classroom_check_record import route_classroom_check_record
from route.teacher.my.activity_check_record import route_activity_check_record
from route.public.login import route_login
from route.public.my import route_my
from route.public.account_manage import route_account_manage
from route.public.suggestion_feedback import route_suggestion_feedback
from route.public.message_push import route_message_push

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

app.register_blueprint(blueprint=route_apply_school_certificate, url_prefix="/student_index/apply_school_certificate")
app.register_blueprint(blueprint=route_apply_classroom, url_prefix="/student_index/apply_classroom")
app.register_blueprint(blueprint=route_apply_activity, url_prefix="/student_index/apply_activity")
app.register_blueprint(blueprint=route_school_certificate_application_record, url_prefix="/student_my/application_record/school_certificate_application_record")
app.register_blueprint(blueprint=route_classroom_application_record, url_prefix="/student_my/application_record/classroom_application_record")
app.register_blueprint(blueprint=route_activity_application_record, url_prefix="/student_my/application_record/activity_application_record")
app.register_blueprint(blueprint=route_check_school_certificate, url_prefix="/teacher_index/check_school_certificate")
app.register_blueprint(blueprint=route_check_classroom, url_prefix="/teacher_index/check_classroom")
app.register_blueprint(blueprint=route_check_activity, url_prefix="/teacher_index/check_activity")
app.register_blueprint(blueprint=route_school_certificate_check_record, url_prefix="/teacher_my/check_record/school_certificate_check_record")
app.register_blueprint(blueprint=route_classroom_check_record, url_prefix="/teacher_my/check_record/classroom_check_record")
app.register_blueprint(blueprint=route_activity_check_record, url_prefix="/teacher_my/check_record/activity_check_record")
app.register_blueprint(blueprint=route_login, url_prefix="/public_login")
app.register_blueprint(blueprint=route_my, url_prefix="/public_my")
app.register_blueprint(blueprint=route_account_manage, url_prefix="/public_my/account_manage")
app.register_blueprint(blueprint=route_suggestion_feedback, url_prefix="/public_my/suggestion_feedback")
app.register_blueprint(blueprint=route_message_push, url_prefix="/message_push")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
