#coding:utf-8

import pdb

from Yep.models import *
from Yep import db_tools
from Yep.response_status import Status
from Yep import system_tags, system_schools
from Yep import tools, qiniu_tools

def init_response_result():
    result = {}
    result["ret"] = Status.OK
    result["info"] = Status().getReason(result["ret"])
    result["data"] = {}
    return result

# 获取系统用户标签列表
def system_user_tag_list():
    return system_tags.tag_list

# 获取热门大学列表
def active_university_list():
    return db_tools.get_active_university_list()

# 获取所有大学列表
def system_university_list():
    return system_schools.school_list

def check_phone(phone):
    result = init_response_result()
    # 检查手机号是否存在
    if not db_tools.check_phone(phone):
        result['ret'] = Status.PHONEEXISTS
        result['info'] = Status().getReason(result['ret'])
    return result

def qiniu_token(key):
    result = init_response_result()
    result['data']['token'] = qiniu_tools.get_qiniu_token(key)
    return result

# 注册
def register(nick, phone, pwd, photo, sex, tag_list, university):
    result = init_response_result()
    # 检查手机号是否存在
    if not db_tools.check_phone(phone):
        result['ret'] = Status.PHONEEXISTS
        result['info'] = Status().getReason(result['ret'])
        return result
    pwd = tools.md5_pwd(pwd)
    result['data'] = db_tools.create_user(nick, phone, pwd, photo, sex, tag_list, university)
    return result

# 登录
def login(phone, pwd):
    pwd = tools.md5_pwd(pwd)
    user_info = db_tools.check_login(phone, pwd)
    result = init_response_result()
    if user_info:
        result['data'] = user_info
    else:
        result['ret'] = Status.PHONEORPWDERROR
        result['info'] = Status().getReason(result['ret'])
    return result

# 切换用户当前活动大学
def switch_active_university(access_token, university):
    result = init_response_result()
    if not db_tools.switch_active_university(access_token, university):
        result['ret'] = Status.UNKNOWNERR
        result['info'] = Status().getReason(result['ret'])
    return result

# 获取Status 列表(讨论,投票,易物,发现)
def status_list(access_token, since_id=-1, max_id=-1, type=-1, count=20, is_follow=0):
    # 获取新的
    if since_id != -1 or max_id == -1:
        return db_tools.get_new_status_list(access_token, since_id, type, count, is_follow)
    return db_tools.get_old_status_list(access_token, max_id, type, count, is_follow)

# 获取评论列表
def comment_list(access_token, status_sha1, max_id):
    return db_tools.comment_list(access_token, status_sha1, max_id)

# 获取Status评论数,点赞数,分享数
def status_count(access_token, status_sha1):
    return db_tools.status_count(access_token, status_sha1)

# 用户参与投票
def join_vote(access_token, vote_sha1, vote_option_index, content):
    return db_tools.join_vote(access_token, vote_sha1, vote_option_index, content)

# 发布一条状态
def publish_status(access_token, title, content, image_list, type, vote_option=[], end_time=3):
    return db_tools.publish_status(access_token, title, content, image_list, type, vote_option=[], end_time=3)