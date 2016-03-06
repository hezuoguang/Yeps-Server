#coding:utf-8
from qiniu import Auth
access_key = "MDWzu5EOTAbqoJp5EGxGcdksEcSLnixxAcGsbv2v"
secret_key = "IujhqwUXdusrrLYooPA4WZdJtS7RR6r65TALg2p_"
bucket_name = "weiliao"

# 获得七牛上传凭证 key 文件名
def get_qiniu_token(key):
    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, key)
    return token