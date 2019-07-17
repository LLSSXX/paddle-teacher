# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Integer, String, Time
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Activity(db.Model):
    __tablename__ = 'activity'

    sequence_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    school_number = db.Column(db.BigInteger)
    college = db.Column(db.String(255))
    profession = db.Column(db.String(255))
    area = db.Column(db.String(255))
    use_date = db.Column(db.Date)
    begin_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    purpose = db.Column(db.String(255))
    submit_time = db.Column(db.DateTime)
    check_method = db.Column(db.String(255))
    result = db.Column(db.String(255))
    isuploading = db.Column(db.String(255))
    check_people_name = db.Column(db.String(255))
    check_people_number = db.Column(db.Integer)


class Classroom(db.Model):
    __tablename__ = 'classroom'

    sequence_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    school_number = db.Column(db.BigInteger)
    college = db.Column(db.String(255))
    profession = db.Column(db.String(255))
    classroom = db.Column(db.String(255))
    use_date = db.Column(db.Date)
    begin_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    purpose = db.Column(db.String(255))
    submit_time = db.Column(db.DateTime)
    check_method = db.Column(db.String(255))
    result = db.Column(db.String(255))
    isuploading = db.Column(db.String(255))
    check_people_name = db.Column(db.String(255))
    check_people_number = db.Column(db.Integer)


class Login(db.Model):
    __tablename__ = 'login'

    username = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(500))
    name = db.Column(db.String(255))
    identity = db.Column(db.String(255))
    college = db.Column(db.String(255))
    profession = db.Column(db.String(255))
    grade = db.Column(db.Integer)


class SchoolCertificate(db.Model):
    __tablename__ = 'school_certificate'

    sequence_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    school_number = db.Column(db.BigInteger)
    choose_college = db.Column(db.String(255))
    profession = db.Column(db.String(255))
    application_reason = db.Column(db.String(255))
    submit_time = db.Column(db.DateTime)
    check_method = db.Column(db.String(255))
    result = db.Column(db.String(255))
    isuploading = db.Column(db.String(255))
    check_people_name = db.Column(db.String(255))
    check_people_number = db.Column(db.Integer)


class SecurityQuestion(db.Model):
    __tablename__ = 'security_question'

    sequence_number = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer)
    question = db.Column(db.String(255))
    answer = db.Column(db.String(255))


class SuggestionFeedback(db.Model):
    __tablename__ = 'suggestion_feedback'

    sequence_number = db.Column(db.Integer, primary_key=True)
    suggestion = db.Column(db.String(255))
    phone_number = db.Column(db.BigInteger)
    submit_time = db.Column(db.DateTime)
