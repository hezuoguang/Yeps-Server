#coding:utf-8
from django.db import models

# Create your models here.

#用户模型
class User(models.Model):
    #sha1 --- phone + time
    sha1 = models.CharField(max_length=40)
    # 用户名
    username = models.CharField(max_length=255)
    # 手机号码
    phone = models.CharField(max_length=11, default="")
    # 密码
    pwd = models.CharField(max_length=32)
    # 昵称
    nick = models.CharField(max_length=255)
    # 邮箱
    email = models.EmailField(null=True)
    # 头像
    photo = models.URLField()
    # 年龄
    age = models.PositiveSmallIntegerField(default = 18)
    # 性别
    sex = models.CharField(max_length = 4, default = "男")
    # 简介
    intro = models.CharField(max_length=255, default="一句话介绍自己^_^")
    # 生日
    birthday = models.DateTimeField(auto_now_add = True)
    # 大学
    university = models.CharField(max_length = 255, default = "怀化学院")
    # 当前活动大学
    active_university = models.CharField(max_length = 255, default = "怀化学院")
    # 注册时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 最后活动时间
    last_active_time = models.DateTimeField(auto_now_add=True)
    # 标签[]
    tag_list = models.TextField(default="[]")
    # 相册[]
    # image_list = models.TextField(default="[]")
    # 授权码
    access_token = models.CharField(max_length=32)


# 已激活的大学
class ActiveUniversity(models.Model):
    university = models.CharField(max_length = 255, default = "怀化学院")
    # 激活时间
    active_time = models.DateTimeField(auto_now_add=True)
    # 激活账户
    user_sha1 = models.CharField(max_length=40)

# 状态
class Status(models.Model):
    # sha1 create_sha1 + time
    sha1 = models.CharField(max_length=40)
    #创建者 user sha1
    user_sha1 = models.CharField(max_length=40)
    # 状态标题
    title = models.CharField(max_length=255)
    # 状态内容
    content = models.TextField()
    # 图片链接 [iamge_url1,image_url2...]
    image_list = models.TextField(blank = True)
    #类型 0:微交流(讨论) 1:微评选(投票) 2:随手拍 3:一起玩 4:发现 5:二手
    type = models.SmallIntegerField(default=0)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 点赞数
    like_count = models.IntegerField(default=0)
    # 分享数
    share_count = models.IntegerField(default=0)
    # 评论数
    comment_count = models.IntegerField(default=0)
    # 状态 0 正常 1 删除
    status = models.IntegerField(default=0)
    # 大学
    university = models.CharField(max_length = 255, default = "怀化学院")

# 投票信息
class Vote(models.Model):
    # sha1 status_sha1 + time
    sha1 = models.CharField(max_length=40)
    # 状态sha1
    status_sha1 = models.CharField(max_length=40)
    # 选项列表[选项1, 选项二]
    vote_option = models.TextField(default="[]")
    # 选项对应的票数[1,10]
    vote_result = models.TextField(default="[]")
    # 当前总票数
    vote_count = models.IntegerField(default=0)
    # 结束时间
    end_time = models.DateTimeField()
    # 是否已经结束
    is_end = models.BooleanField(default=False)

# 个人投票记录
class VoteRecord(models.Model):
    vote_sha1 = models.CharField(max_length=40)
    user_sha1 = models.CharField(max_length=40)
    # 所投选项
    vote_option_index = models.SmallIntegerField()
    # 附件说明
    content = models.CharField(max_length=255,default="")
    # 投票时间
    create_time = models.DateTimeField(auto_now_add=True)

# 点赞记录
class Like(models.Model):
    user_sha1 = models.CharField(max_length=40)
    status_sha1 = models.CharField(max_length=40)
    create_time = models.DateTimeField(auto_now_add=True)
# 评论
class Comment(models.Model):
    # sha1 create_sha1 + status_sha1 + time
    sha1 = models.CharField(max_length=40)
    # 所评论状态sha1
    status_sha1 = models.CharField(max_length=40)
    user_sha1 = models.CharField(max_length=40)
    # 评论内容
    content = models.CharField(max_length=1024)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 是否为子评论
    is_sub = models.BooleanField(default=False)
    # 父评论sha1
    comment_sha1 = models.CharField(max_length=40, null=True)
    # 状态 0 正常 1 删除
    status = models.IntegerField(default=0)

# 用户关系表(关注)
class Follow(models.Model):
    user_sha1 = models.CharField(max_length=40)
    other_user_sha1 = models.CharField(max_length=40)
    create_time = models.DateTimeField(auto_now_add=True)

# 消息
class Message(models.Model):
    # user_sha1 + other_sha1 + time
    sha1 = models.CharField(max_length=40)
    # 消息通知者
    user_sha1 = models.CharField(max_length=40)
    # 消息产生者
    other_sha1 = models.CharField(max_length=40)
    # 消息内容
    content = models.CharField(max_length=255)
    # 消息状态 0 未读, 1 已读, 2 删除
    status = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)


# 匹配(交友)
class Match(models.Model):
    user_sha1 = models.CharField(max_length=40)
    other_user_sha1 = models.CharField(max_length=40)
    # 喜欢:1, 不喜欢0
    option = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

