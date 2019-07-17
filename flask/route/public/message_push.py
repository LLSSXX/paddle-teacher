from flask import Blueprint, request, json
import hashlib

import urllib.request as urllib


route_message_push = Blueprint(name="route_message_push", import_name=__name__)


# 消息推送
@route_message_push.route('/send_message_push', methods=['GET'])
def send_message_push():
    # signature = request.values.get("signature")
    # timestamp = request.values.get("timestamp")
    # nonce = request.values.get("nonce")
    # token = "19990806"
    # echostr = request.values.get("echostr")
    # info = [token, timestamp, nonce]
    # info_new = sorted(info)
    # str_new = ''.join(info_new)
    # tmpStr = hashlib.sha1()
    # tmpStr.update(str_new.encode('utf-8'))
    # tmpStr_new = tmpStr.hexdigest()  # 获取加密串
    # if tmpStr_new == signature:
    #     return echostr
    # else:
    #     return "false"

    signature = request.values.get("signature")
    timestamp = request.values.get("timestamp")
    nonce = request.values.get("nonce")
    echostr = request.values.get("echostr")
    token = "19990806"
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    if hashcode == signature:
        return echostr
    else:
        return "false"

    return echostr
