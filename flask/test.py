

# # 创建密文密码（注册）
# @route_login.route('/register', methods=['POST'])
# def register():
#     username = int(json.loads(request.values.get("username")))
#     password = str(json.loads(request.values.get("password")))
#     pw_hash = generate_password_hash(password)
#     db.engine.execute("update `login` set password = %s where username = %s", (pw_hash, username))
#     return "创建密文密码成功"


# import hashlib
# import urllib.request as urllib
# import json
# # signature = str(json.loads(request.values.get("signature")))
# # timestamp = str(json.loads(request.values.get("timestamp")))
# # nonce = str(json.loads(request.values.get("nonce")))
# # token = str(json.loads(request.values.get("token")))
# # echostr = str(json.loads(request.values.get("echostr")))
# signature = "ajsjdnnc32929dend"
# timestamp = "ajdncZnsxns"
# nonce = "Asxxds"
# token = "Sxxnsxnisxdi"
# echostr = "sxisisnxnsAskx"
# info = [token, timestamp, nonce]
# info_new = sorted(info)
# str_new = ''.join(info_new)
# tmpStr = hashlib.sha1()
# tmpStr.update(str_new.encode('utf-8'))
# tmpStr_new = tmpStr.hexdigest() #获取加密串
# # if tmpStr == signature:
# #     return json.dumps(echostr)
# # else:
# #     return False
# print(info)
# print(info_new)
# print(str_new)
# print(tmpStr_new)
#
#
# doc = urllib.urlopen("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxca9c32c5b47a5454&secret=edc8c4d71cdb4131d27728e305a8a1c9").read()
# b = json.loads(doc)
# print(b)
#
# z = urllib.urlopen("https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token=20_5hi1CyR1U7OVZl7Tfhew1nXx6lvoOPJoPuvohTfE4SPIxzfzhgxrwkjeqGQ3fJzgRezbZ_G9lgFLq0puzBf_6q0pEfflMiyZmP4W8yWbhSvlA0TndKH1HO0rU8Rma_Y6v69tEhUhHi4WGSJFCYTjAAAGCX").read()
# a = json.loads(z)
# print(a)

from werkzeug.security import generate_password_hash
password = "2030200114"
pw_hash = generate_password_hash(password)
print(pw_hash)
