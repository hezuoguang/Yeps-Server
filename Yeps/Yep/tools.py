#coding:utf-8

import hashlib, datetime, pdb

from Yep import system_tags, system_schools

MD5PERFIX = "YEPS_WEIMI"

def md5_pwd(pwd):
    return hashlib.new("md5", MD5PERFIX + pwd).hexdigest()

# 检查标签是否合法
def check_user_tag(tags):
    tag_list = system_tags.tag_list
    for tag in tags:
        if tag not in tag_list:
            return False
    return True

# 检查学校是否合法
def check_school(school):
    school_list = system_schools.school_list
    if school in school_list:
        return True
    return False

# 计算sha1
def sha1_with_args(*kwargs):
    sha1 = hashlib.sha1()
    for arg in kwargs:
        sha1.update(arg)
    sha1 = sha1.hexdigest()
    return sha1

# 计算access_token
def init_access_token(user_sha1, pwd):
    return hashlib.new("md5", MD5PERFIX + user_sha1 + pwd).hexdigest()

# datetime to "XXXX-XX-XX : XX:XX:XX"
def date_time_to_str(t):
    return t.strftime("%Y-%m-%d %H:%M:%S")