from flask import Blueprint, request, json
from mysql import *


route_suggestion_feedback = Blueprint(name="route_suggestion_feedback", import_name=__name__)


# 我的-意见反馈
@route_suggestion_feedback.route('/submit_suggestion_feedback', methods=['POST'])
def submit_suggestion_feedback():
    suggestion = str(json.loads(request.values.get("suggestion")))
    phone_number = int(json.loads(request.values.get("phone_number")))
    date_time = str(json.loads(request.values.get("date_time")))
    res = SuggestionFeedback(suggestion=suggestion, phone_number=phone_number, submit_time=date_time)
    db.session.add(res)
    db.session.commit()

    return '意见反馈'