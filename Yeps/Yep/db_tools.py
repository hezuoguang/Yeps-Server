#coding:utf-8

import hashlib, datetime, json, pdb
from django.db import transaction
from Yep.models import *
from Yep.response_status import Status as ReStatus
from Yep.response_status import ZGError
from Yep import tools
def check_phone(phone):
    user = User.objects.filter(phone=phone).first()
    if user:
        return False
    return True

# 获取热门学校列表
def get_active_university_list():
    active_universitys = ActiveUniversity.objects.all()
    university_list = []
    for active_university in active_universitys:
        university_list.append(active_university.university)
    return university_list

# 获取用户基本信息
def get_user_basic_info(user_sha1):
    user = User.objects.get(sha1=user_sha1)
    user_info = dict(
        user_sha1 = user.sha1,
        nick = user.nick,
        photo = user.photo
    )
    return user_info

# 获取用户信息,不包括access_token
def get_user_info(user_sha1):
    user_info = get_user_full_info(user_sha1)
    user_info.pop("access_token")
    return user_info

#获取其他用户资料
def get_other_info(access_token, other_user_sha1):
    user = user_with_access_token(access_token)
    return get_other_info_with_user_sha1(user.sha1, other_user_sha1)

#获取其他用户资料
def get_other_info_with_user_sha1(user_sha1, other_user_sha1):
    other_user_info = get_user_info(other_user_sha1)
    followR = Follow.objects.filter(user_sha1=user_sha1, other_user_sha1=other_user_sha1)
    if followR:
        other_user_info['is_follow'] = 1
    else:
        other_user_info['is_follow'] = 0
    return other_user_info

# 检测用户登录, 成功返回用户信息 失败返回False
def check_login(phone, pwd):
    try:
        user = User.objects.get(phone=phone, pwd=pwd)
        return get_user_full_info(user.sha1)
    except Exception,e:
        return False

#获取用户所有信息
def get_user_full_info(user_sha1):
    user = User.objects.get(sha1=user_sha1)
    # "follow_count" : "关注数",
    # "fans_count" : "粉丝数",
    # "status_count" : "状态数",
    status_count = Status.objects.filter(user_sha1=user_sha1).count()
    fans_count = Follow.objects.filter(other_user_sha1=user_sha1).count()
    follow_count = Follow.objects.filter(user_sha1=user_sha1).count()
    status_image_count = UserImage.objects.filter(user_sha1=user_sha1).count()
    age = datetime.datetime.now().year - user.birthday.year
    if age < 0:
        age = 0
    user_info = dict(
        user_sha1 = user.sha1,
        nick = user.nick,
        phone = user.phone,
        photo = user.photo,
        email = user.email,
        age = age,
        sex = user.sex,
        intro = user.intro,
        birthday = user.birthday.strftime("%Y-%m-%d"),
        university = user.university,
        active_university = user.active_university,
        tag_list = json.loads(user.tag_list),
        create_time = tools.date_time_to_str(user.create_time),
        last_active_time = tools.date_time_to_str(user.last_active_time),
        access_token = user.access_token,
        status_count = status_count,
        fans_count = fans_count,
        follow_count =follow_count,
        image_list = json.loads(user.image_list),
        status_image_count = status_image_count
    )
    return user_info

# 创建一个用户
@transaction.commit_on_success()
def create_user(nick, phone, pwd, photo, sex, tag_list, university):
    now = datetime.datetime.now()
    sha1 = tools.sha1_with_args(phone, str(now))
    user = User()
    user.pwd = pwd
    user.nick = nick
    user.sha1 = sha1
    user.phone = phone
    user.photo = photo
    user.sex = sex
    user.tag_list = json.dumps(tag_list)
    user.university = university
    user.active_university = university
    user.access_token = tools.init_access_token(sha1, pwd)
    user.save()
    active_university = ActiveUniversity.objects.filter(university=university).first()
    if not active_university:
        active_university = ActiveUniversity()
        active_university.university = university
        active_university.user_sha1 = sha1
        active_university.save()
    user_info = get_user_full_info(user.sha1)
    return user_info

# 根据access_token 获得用user
def user_with_access_token(access_token):
    try:
        user = User.objects.get(access_token=access_token)
        return user
    except Exception,e:
        return False

# 切换用户当前活动大学
def switch_active_university(access_token, university):
    try:
        user = user_with_access_token(access_token)
        user.active_university = university
        user.save()
        return True
    except Exception,e:
        return False

# 获取用户关注用户sha1列表
def get_follow_list(user_sha1):
    follows = Follow.objects.filter(user_sha1=user_sha1)
    sha1_list = []
    sha1_list.append(user_sha1)
    for follow in follows:
        sha1_list.append(follow.other_user_sha1)
    return sha1_list


# 获取id 大于sinace_id的status数据
def get_new_status_list(access_token, sinace_id, type, count, is_follow):
    user = user_with_access_token(access_token)
    if is_follow != 0:
        sha1_list = get_follow_list(user.sha1)
        if sinace_id != -1:
            statuses = Status.objects.filter(id__gt=sinace_id,status=0).filter(user_sha1__in=sha1_list).order_by("id")[0:count]
            statuses = sorted(statuses, key=lambda s1:-s1.id)[0 : count]
        else:
            statuses = Status.objects.filter(status=0).filter(user_sha1__in=sha1_list).order_by("-id")[0:count]
    else:
        if sinace_id != -1:
            statuses = Status.objects.filter(id__gt=sinace_id, type=type, status=0,university=user.active_university).order_by("id")[0:count]
            statuses = sorted(statuses, key=lambda s1:-s1.id)[0 : count]
        else:
            statuses = Status.objects.filter(type=type, status=0,university=user.active_university).order_by("-id")[0:count]
    status_list = []
    for status in statuses:
        tmp = status_to_dict(user, status)
        status_list.append(tmp)
    return status_list

# 获取id 小于max_id的status数据
def get_old_status_list(access_token, max_id, type, count, is_follow):
    user = user_with_access_token(access_token)
    if is_follow != 0:
        sha1_list = get_follow_list(user.sha1)
        statuses = Status.objects.filter(id__lt=max_id, type=type, status=0).filter(user_sha1__in=sha1_list).order_by("-id")[0:count]
    else:
        statuses = Status.objects.filter(id__lt=max_id, type=type, status=0,university=user.active_university).order_by("-id")[0:count]
    status_list = []
    for status in statuses:
        tmp = status_to_dict(user, status)
        status_list.append(tmp)
    return status_list

# 获取id 大于sinace_id的status数据
def get_new_user_status_list(access_token, user_sha1, sinace_id, count):
    # user = user_with_access_token(access_token)
    user = User.objects.get(sha1=user_sha1)
    if sinace_id != -1:
        statuses = Status.objects.filter(id__gt=sinace_id, status=0, user_sha1=user_sha1).order_by("id")[0:count]
        statuses = sorted(statuses, key=lambda s1:-s1.id)[0 : count]
    else:
        statuses = Status.objects.filter(status=0, user_sha1=user_sha1).order_by("-id")[0:count]
    status_list = []
    for status in statuses:
        tmp = status_to_dict(user, status)
        status_list.append(tmp)
    return status_list

# 获取id 小于max_id的status数据
def get_old_user_status_list(access_token,user_sha1, max_id, count):
    user = user_with_access_token(access_token)
    statuses = Status.objects.filter(id__lt=max_id, status=0, user_sha1=user_sha1).order_by("-id")[0:count]
    status_list = []
    for status in statuses:
        tmp = status_to_dict(user, status)
        status_list.append(tmp)
    return status_list

# 获取status 的详细信息,以字典形式返回
def status_to_dict(user, status, is_detail=False):
    tmp = {}
    create_user = User.objects.filter(sha1=status.user_sha1).first()
    tmp["status_id"] = status.id
    tmp["status_sha1"] = status.sha1
    tmp["title"] = status.title
    content = status.content
    # if not is_detail:
    #     if len(content) > 60:
    #         content = content[0:60] + "..."
    tmp["content"] = content
    try:
        tmp["image_list"] = json.loads(status.image_list)
    except Exception,e:
        tmp["image_list"] = []
    tmp["type"] = status.type
    tmp["create_time"] = tools.date_time_to_str(status.create_time)
    tmp["like_count"] = status.like_count
    tmp["share_count"] = status.share_count
    tmp["comment_conut"] = status.comment_count
    tmp["university"] = status.university
    tmp["create_user"] = {
        'user_sha1': create_user.sha1,
        'nick': create_user.nick,
        'photo': create_user.photo
    }

    like = Like.objects.filter(user_sha1=user.sha1, status_sha1=status.sha1).first()
    if like:
        tmp["me_is_like"] = True
    else:
        tmp["me_is_like"] = False
    if status.type == 1:
        vote = Vote.objects.filter(status_sha1=status.sha1).first()
        if not vote.is_end:
            if vote.end_time <= datetime.datetime.now():
                vote.is_end = True
                vote.save()
        tmp["vote"] = vote_to_dict(user.sha1,status_sha1=status.sha1)
    return tmp

# user_sha1 和 status_sha1/vote_sha1 获取投票详情
def vote_to_dict(user_sha1, status_sha1=None, vote_sha1=None):
    vote = None
    if status_sha1:
        vote = Vote.objects.filter(status_sha1=status_sha1).first()
    elif vote_sha1:
        vote = Vote.objects.filter(sha1=vote_sha1).first()
    else:
        raise ValueError
    tmp = {
            'vote_sha1': vote.sha1,
            'vote_result': json.loads(vote.vote_result),
            'vote_option': json.loads(vote.vote_option),
            'vote_count': vote.vote_count,
            'end_time': tools.date_time_to_str(vote.end_time),
            'is_end': vote.is_end,
        }
    record = VoteRecord.objects.filter(user_sha1=user_sha1, vote_sha1=vote.sha1).first()
    if record:
        tmp['me_is_vote'] = True
        tmp['me_vote_option'] = record.vote_option_index
    else:
        tmp['me_is_vote'] = False
    return tmp

# 获取评论的详细信息
def comment_to_dict(comment):
    tmp = {
        'create_user':get_user_basic_info(comment.user_sha1),
        'comment_id': comment.id,
        'comment_sha1': comment.sha1,
        'content': comment.content,
        'create_time': tools.date_time_to_str(comment.create_time),
        'is_sub': comment.is_sub
    }
    if comment.is_sub:
        other_comment = Comment.objects.get(sha1=comment.comment_sha1)
        tmp['other_user'] = get_user_basic_info(other_comment.user_sha1)
    return tmp
#获取status详情
def status_detail(access_token, status_sha1):
    user = user_with_access_token(access_token)
    status = Status.objects.get(sha1=status_sha1)
    return status_to_dict(user, status,True)

# 获取评论列表
def comment_list(access_token, status_sha1, max_id):
    if max_id == -1:
        comments = Comment.objects.filter(status_sha1=status_sha1, status=0).order_by('-id')[0:20]
    else:
        comments = Comment.objects.filter(status_sha1=status_sha1, id__lt=max_id, status=0).order_by('-id')[0:20]
    com_list = []
    for comment in comments:
        #id小的在前
        com_list.insert(0,comment_to_dict(comment))
    return com_list

# 获取Status评论数,点赞数,分享数
def status_count(access_token, status_sha1):
    user = user_with_access_token(access_token)
    status = Status.objects.get(sha1=status_sha1)
    tmp = {
        'like_count': status.like_count,
        'share_count': status.share_count,
        'comment_conut': status.comment_count
    }
    like = Like.objects.filter(user_sha1=user.sha1, status_sha1=status.sha1).first()
    if like:
        tmp["me_is_like"] = True
    else:
        tmp["me_is_like"] = False
    return tmp

# 用户参与投票
def join_vote(access_token, vote_sha1, vote_option_index, content):
    vote = Vote.objects.get(sha1=vote_sha1)
    user = user_with_access_token(access_token)
    if vote.end_time < datetime.datetime.now():
        vote.is_end = True
        vote.save()
    if vote.is_end:
        tmp = {
            "ret" : ReStatus.VOTEENDERRPOR,
            "info": ReStatus().getReason(ReStatus.VOTEENDERRPOR),
            "data": {
                "vote": vote_to_dict(user.sha1, vote_sha1=vote_sha1)
            }
        }
        return tmp
    record = VoteRecord.objects.filter(user_sha1=user.sha1, vote_sha1=vote.sha1).first()
    if record:
        tmp = {
            "ret" : ReStatus.VOTEREPEATERRPOR,
            "info": ReStatus().getReason(ReStatus.VOTEREPEATERRPOR),
            "data": {
                "vote": vote_to_dict(user.sha1, vote_sha1=vote_sha1)
            }
        }
        return tmp
    if vote_option_index >= len(json.loads(vote.vote_option)):
        raise ValueError
    record = VoteRecord()
    record.vote_sha1 = vote.sha1
    record.user_sha1 = user.sha1
    record.vote_option_index = vote_option_index
    record.content = content
    vote.vote_count = vote.vote_count + 1
    vote_result = json.loads(vote.vote_result)
    vote_result[vote_option_index] = vote_result[vote_option_index] + 1
    vote.vote_result = json.dumps(vote_result)
    vote.save()
    record.save()
    tmp = vote_to_dict(user.sha1, vote_sha1=vote_sha1)
    return tmp

# 发布一条状态
def publish_status(access_token, title, content, image_list, type, vote_option=[], end_time=3):
    user = user_with_access_token(access_token)
    status = Status()
    status.user_sha1 = user.sha1
    status.sha1 = tools.sha1_with_args(user.sha1, str(datetime.datetime.now()))
    status.title = title
    status.content = content
    status.image_list = json.dumps(image_list)
    status.type = type
    status.university = user.university
    if type == 1:
        vote = Vote()
        vote.sha1 = tools.sha1_with_args(status.sha1, str(datetime.datetime.now()))
        vote.vote_option = json.dumps(vote_option)
        vote.status_sha1 = status.sha1
        vote_result = []
        # 结束时间(0:6小时后, 1:12小时后, 2:1天后, 3:3天后, 4:7天后)
        time_list = [6, 12, 24, 72, 168]
        if end_time >= len(time_list):
            end_time = len(time_list) - 1
        end_time = datetime.datetime.now() + datetime.timedelta(hours=time_list[end_time])
        vote.end_time = end_time

        for i in range(len(vote_option)):
            vote_result.append(0)
        vote.vote_result = json.dumps(vote_result)
        vote.save()
    status.save()
    for image_url in image_list:
        userImage = UserImage()
        userImage.user_sha1 = user.sha1
        userImage.status_sha1 = status.sha1
        userImage.image_url = image_url
        userImage.save()

    return status_to_dict(user, status)

# 发布一条评论
def publish_comment(access_token, content, status_sha1, comment_sha1):
    user = user_with_access_token(access_token)
    status = Status.objects.get(sha1=status_sha1)

    now = datetime.datetime.now()
    sha1 = tools.sha1_with_args(status_sha1, user.sha1, str(now))

    comment = Comment()
    comment.sha1 = sha1
    comment.status_sha1 = status_sha1
    comment.user_sha1 = user.sha1
    comment.content = content
    comment.comment_sha1 = ""
    if comment_sha1:
        comment.is_sub = True
        comment.comment_sha1 = comment_sha1
    comment.save()
    status.comment_count += 1
    status.save()
    data = dict()
    data['comment'] = comment_to_dict(comment)
    data.update(status_count(access_token, status_sha1))

    return data

# 点赞/取消点赞
def click_like(access_token, status_sha1):
    user = user_with_access_token(access_token)
    status = Status.objects.get(sha1=status_sha1)
    like = Like.objects.filter(user_sha1=user.sha1,status_sha1=status_sha1)
    if like.count() != 0:
        status.like_count -= like.count()
        like.delete()
    else:
        like = Like()
        like.status_sha1 = status_sha1
        like.user_sha1 = user.sha1
        like.save()
        status.like_count += 1
    status.save()
    data = status_count(access_token, status_sha1)
    return data

# 分享成功
def share_count_add(access_token, status_sha1):
    user = user_with_access_token(access_token)
    status = Status.objects.get(sha1=status_sha1)
    status.share_count += 1
    status.save()
    return status_count(access_token, status_sha1)

# 关注
def follow(access_token, user_sha1):
    user = user_with_access_token(access_token)
    if user.sha1 == user_sha1:
        raise ValueError
    other_user = User.objects.get(sha1=user_sha1)
    followShip = Follow.objects.filter(user_sha1=user.sha1, other_user_sha1=other_user.sha1).first()
    if followShip:
        return {}
    followShip = Follow()
    followShip.user_sha1 = user.sha1
    followShip.other_user_sha1 = other_user.sha1
    followShip.save()
    return {}

# 取消关注
def remove_follow(access_token, user_sha1):
    user = user_with_access_token(access_token)
    if user.sha1 == user_sha1:
        raise ValueError
    other_user = User.objects.get(sha1=user_sha1)
    Follow.objects.filter(user_sha1=user.sha1, other_user_sha1=other_user.sha1).delete()
    return {}

# 更新头像
def update_photo(access_token, photo):
    user = user_with_access_token(access_token)
    user.photo = photo
    user.save()
    # return get_user_full_info(user.sha1)
    return {}

# 更新个人页面背景图片
def update_profile_back(access_token, photo):
    user = user_with_access_token(access_token)
    image_list = json.loads(user.image_list)
    if len(image_list) == 0:
        image_list.append(photo)
    else:
        image_list[0] = photo
    user.image_list = json.dumps(image_list)
    user.save()
    # return get_user_full_info(user.sha1)
    return {}

# 更新用户标签
def update_tag_list(access_token, tag_list):
    user = user_with_access_token(access_token)
    user.tag_list = json.dumps(tag_list)
    user.save()
    return get_user_info(user.sha1)

# 更新密码
def update_pwd(access_token, old_pwd, new_pwd):
    user = user_with_access_token(access_token)
    old_pwd = tools.md5_pwd(old_pwd)
    if old_pwd != user.pwd:
        raise ZGError(ReStatus.OLDPWDERROR)
    new_pwd = tools.md5_pwd(new_pwd)
    user.pwd = new_pwd
    user.access_token = tools.init_access_token(user.sha1, new_pwd)
    user.save()
    return {}

#更新用户简介
def update_intro(access_token, intro):
    user = user_with_access_token(access_token)
    user.intro = intro
    user.save()
    return get_user_info(user.sha1)

#更新用户信息
def update_info(access_token, nick, email, sex, birthday):
    user = user_with_access_token(access_token)
    user.nick = nick
    user.email = email
    user.sex = sex
    user.birthday = birthday
    user.save()
    return get_user_info(user.sha1)

# 获取自己资料
def get_self_info(access_token):
    user = user_with_access_token(access_token)
    return get_user_info(user.sha1)

#获取其他用信息
def get_other_user_info(access_token, user_sha1):
    return get_other_info(access_token, user_sha1)

# 获取用户状态照片列表
def status_image_list(access_token, user_sha1, max_id):
    user = User.objects.get(sha1=user_sha1)
    if max_id != -1:
        userImages = UserImage.objects.filter(id__lt=max_id, user_sha1=user.sha1).order_by("-id")[0:30]
    else:
        userImages = UserImage.objects.filter(user_sha1=user.sha1).order_by("-id")[0:30]
    image_list = []
    for userImage in userImages:
        tmp = {}
        tmp['status_sha1'] = userImage.status_sha1
        tmp['image_id'] = userImage.id
        tmp['image_url'] = userImage.image_url
        image_list.append(tmp)
    return image_list

#匹配过的user_sha1_list
def match_after_user_list(user_sha1):
    matchs = Match.objects.filter(user_sha1=user_sha1)
    sha1_list = []
    sha1_list.append(user_sha1)
    for match in matchs:
        sha1_list.append(match.other_user_sha1)
    return sha1_list

# 获取系统推荐用户列表
def recommend_user_list(access_token, max_id, count):
    user = user_with_access_token(access_token)
    sha1_list = match_after_user_list(user.sha1)
    sex = user.sex
    if max_id == -1:
        users = User.objects.all().exclude(sex=sex).exclude(sha1__in=sha1_list).order_by("-id")[0:count]
    else:
        users = User.objects.filter(id__lt=max_id).exclude(sex=sex).exclude(sha1__in=sha1_list,sex=sex).order_by("-id")[0:count]
    user_list = []
    for u in users:
        info = get_other_info_with_user_sha1(user.sha1, u.sha1)
        info['recommend_id'] = u.id
        user_list.append(info)
    return user_list

# 创建消息
def create_message(user_sha1, other_user_sha1, content):
    now = datetime.datetime.now()
    sha1 = tools.sha1_with_args(user_sha1, other_user_sha1, str(now))
    message = Message()
    message.sha1 = sha1
    message.user_sha1 = user_sha1
    message.other_sha1 = other_user_sha1
    message.content = content
    message.save()

# 匹配操作
def match_option(access_token, user_sha1, is_match):
    other_user = User.objects.get(sha1=user_sha1)
    user = user_with_access_token(access_token)
    match = Match.objects.filter(user_sha1=user.sha1, other_user_sha1=other_user.sha1).first()
    if match:
        return {}
    if is_match != 0:
        is_match = 1
    match = Match()
    match.user_sha1 = user.sha1
    match.other_user_sha1 = other_user.sha1
    match.option = is_match
    match.save()
    success = Match.objects.filter(user_sha1=other_user.sha1, other_user_sha1=user.sha1, option=1).first()
    if success:
        content = '匹配成功'
        create_message(user.sha1, other_user.sha1, content)
        create_message(other_user.sha1, user.sha1, content)
    return {}
