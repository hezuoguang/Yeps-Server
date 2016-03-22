#coding:utf-8
from qiniu import Auth
access_key = "Q87pKtapt7ZliPHSdkbQsIlpsWTIM-PqB1VYRvSN"
secret_key = "KQKYhmgJTPO5J4rRsQMGZOyOfmPZEwiD0b8_BgTm"
bucket_name = "yeps"

# 获得七牛上传凭证 key 文件名
def get_qiniu_token(key):
    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, key)
    return token