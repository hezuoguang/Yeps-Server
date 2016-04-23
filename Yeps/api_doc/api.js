/*
Yeps接口文档
创建时间：2016-02-27
*/

var api_data = [

    // 获取系统用户标签列表
    {
        "name": "获取系统用户标签列表",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "system_user_tag_list",
            "data": {
                
            }
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            "data":{
                "tag_list":[
                    "Python",
                    "IOS"
                ],
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
        }
    },

    // 获取热门大学列表
    {
        "name": "获取热门大学列表",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "active_university_list",
            "data": {
                
            }
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            "data":{
                "university_list":[
                    "北京大学",
                    "北京林业大学",
                    "湖南大学",
                    "怀化学院"
                ],
                "total_count":"",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
        }
    },

    // 获取所有大学列表
    {
        "name": "获取所有大学列表",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "system_university_list",
            "data": {
                
            }
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            "data":{
                "university_list":[
                    "北京大学",
                    "北京林业大学",
                    "湖南大学",
                    "怀化学院"
                ],
                "total_count":"",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
        }
    },

    // 获得七牛上传token
    {
        "name": "获得七牛上传token",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "qiniu_token",
            "data": {
                'pic_name': '上传后图片名称',
            }
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            "data":{
                'token': 'token',
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
        }
    },

    // 检查手机号是否被注册
    {
        "name": "检查手机号是否被注册",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "check_phone",
            "data": {
                "phone":"手机号码",
            }
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            "data":{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
        }
    },

    // 注册
    {
        "name": "注册",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "register",
            "data": {
                "phone":"手机号码",
                "nick":"昵称",
                "pwd":"密码(MD5加密后上传)",
                "photo":"头像url",
                "sex":"性别(0:男, 1:女)",
                "tag_list":"标签列表[Python, IOS...]",
                "university":"大学(注册后无法修改)",
            }
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            "data":{
                "user_sha1":"用户sha1",
                "nick":"昵称",
                "phone":"手机号码",
                "photo":"头像url",
                "email":"邮箱",
                "age":"年(22)",
                "sex":"性别(男,女)",
                "intro":"个人简介",
                "birthday":"生日",
                "university":"大学",
                "active_university":"当前活动学校",
                "tag_list":"标签列表[Python, IOS...](字符串)",
                "create_time":"注册时间(2016-02-27 18:25:30)",
                "last_active_time":"最后活动时间(2016-02-27 18:25:30)",
                "follow_count" : "关注数",
                "fans_count" : "粉丝数",
                "status_count" : "状态数",
                "access_token":"授权码",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
        }
    },

    // 登录
    {
        "name": "登录",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "login",
            "data": {
                "phone":"",
                "pwd":"MD5加密后上传"
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "user_sha1":"用户sha1",
                "nick":"昵称",
                "phone":"手机号码",
                "photo":"头像url",
                "email":"邮箱",
                "age":"年(22)",
                "sex":"性别(男,女)",
                "intro":"个人简介",
                "birthday":"生日",
                "university":"大学",
                "active_university":"当前活动学校",
                "tag_list":"标签列表[Python, IOS...]",
                "create_time":"注册时间(2016-02-27 18:25:30)",
                "last_active_time":"最后活动时间(2016-02-27 18:25:30)",
                "follow_count" : "关注数",
                "fans_count" : "粉丝数",
                "status_count" : "状态数",
                "access_token":"授权码",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 切换用户当前活动大学
    {
        "name": "切换用户当前活动大学",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "switch_active_university",
            "data": {
                "access_token":"授权码",
                "university":"此字段回去匹配Status.university, 若用户想获取其他大学的Status,需先更新次字段",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    //获取Status 列表(讨论,投票,二手,发现...)
    {
        "name": "获取Status 列表(讨论,投票,易物,发现)",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "status_list",
            "data": {
                "access_token":"授权码",
                "since_id":"status_id(获取status_id > since_id的数据,可选,不选则获取最新的)",
                "max_id":"status_id(获取status_id < max_id的最新数据,可选,若此参数填写,则since_id无效)",
                "type":"类型 0:微交流(讨论) 1:微评选(投票) 2:随手拍 3:一起玩 4:发现 5:二手",
                "count":"单页返回的记录条数，最大不超过50，默认为20",
                "is_follow":"是否只查询关注的好友和自己的Status(0:不是 1:是,默认不是)",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "status_list":[
                    {
                        "create_user":{
                            "user_sha1":"user_sha1",
                            "nick":"昵称",
                            "photo":"头像url",
                        },
                        "status_id":"",
                        "status_sha1":"Status_sha1",
                        "title":"标题",
                        "content":"详细内容",
                        "image_list":"图片url_list[http://XXX.com/XXX.png,...]",
                        "type":"类型 0:微交流(讨论) 1:微评选(投票) 2:随手拍 3:一起玩 4:发现 5:二手",
                        "create_time":"创建时间(2016-02-27 18:21:34)",
                        "like_count":"点赞数",
                        "share_count":"分享数",
                        "comment_conut":"评论数",
                        "university":"大学",
                        "me_is_like":"我是否点过赞",
                    },
                    {
                        "create_user":{
                            "user_sha1":"user_sha1",
                            "nick":"昵称",
                            "photo":"头像url",
                        },
                        "status_id":"",
                        "status_sha1":"Status_sha1",
                        "title":"标题",
                        "content":"详细内容",
                        "image_list":"图片url_list[http://XXX.com/XXX.png,...]",
                        "type":"1:微评选",
                        "create_time":"创建时间(2016-02-27 18:21:34)",
                        "like_count":"点赞数",
                        "share_count":"分享数",
                        "comment_conut":"评论数",
                        "university":"大学",
                        "me_is_like":"我是否点过赞",
                        "vote":{
                            "vote_sha1":"",
                            "vote_option":"选项列表[选项1, 选项二]",
                            "vote_result":"选项对应的票数[1,10]",
                            "vote_count":"当前总票数",
                            "me_is_vote":"我是否参与了投票(0:未参与, 1:参与了)",
                            "me_vote_option":"我投的选项下标",
                            "end_time":"结束时间",
                            "is_end":"是否已经结束(0:未结束, 1:已结束)",
                        }
                    }
                ],
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    //获取Status 详情
    {
        "name": "获取Status详情",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "status_detail",
            "data": {
                "access_token":"授权码",
                "status_sha1":"",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "status":{
                    "create_user":{
                        "user_sha1":"user_sha1",
                        "nick":"昵称",
                        "photo":"头像url",
                    },
                    "status_id":"",
                    "status_sha1":"Status_sha1",
                    "title":"标题",
                    "content":"详细内容",
                    "image_list":"图片url_list[http://XXX.com/XXX.png,...]",
                    "type":"1:微评选",
                    "create_time":"创建时间(2016-02-27 18:21:34)",
                    "like_count":"点赞数",
                    "share_count":"分享数",
                    "comment_conut":"评论数",
                    "university":"大学",
                    "me_is_like":"我是否点过赞",
                    "vote":{
                        "vote_sha1":"",
                        "vote_option":"选项列表[选项1, 选项二]",
                        "vote_result":"选项对应的票数[1,10]",
                        "vote_count":"当前总票数",
                        "me_is_vote":"我是否参与了投票(0:未参与, 1:参与了)",
                        "me_vote_option":"我投的选项下标",
                        "end_time":"结束时间",
                        "is_end":"是否已经结束(0:未结束, 1:已结束)",
                    }
                }
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 获取评论列表
    {
        "name": "获取评论列表",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "comment_list",
            "data": {
                "access_token":"授权码",
                "max_id":"commen_id(commen_id < max_id的最新评论,可选,默认获取最新评论)",
                "status_sha1":"status_sha1",
            }
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            "data":{
                "comment_list":[
                    {
                        "create_user":{
                            "user_sha1":"user_sha1",
                            "nick":"昵称",
                            "photo":"头像url",
                        },
                        "comment_id":"",
                        "comment_sha1":"comment_sha1",
                        "content":"评论内容",
                        "create_time":"创建时间(2016-02-27 18:21:34)",
                        "is_sub":"是否为子评论(0:不是 1:是)",
                    },
                    {
                        "create_user":{
                            "user_sha1":"user_sha1",
                            "nick":"昵称",
                            "photo":"头像url",
                        },
                        "comment_id":"",
                        "comment_sha1":"comment_sha1",
                        "content":"评论内容",
                        "create_time":"创建时间(2016-02-27 18:21:34)",
                        "is_sub":"1",
                        "other_user":{
                            "user_sha1":"user_sha1",
                            "nick":"昵称",
                            "photo":"头像url",
                        }
                    }
                ],
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
        }
    },

    // 获取Status评论数,点赞数,分享数
    {
        "name": "获取Status评论数,点赞数,分享数",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "status_count",
            "data": {
                "access_token":"授权码",
                "status_sha1":"status_sha1",
            }
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            "data":{
                "like_count":"点赞数",
                "share_count":"分享数",
                "comment_conut":"评论数",
                "me_is_like":"我是否点过赞",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
        }
    },

    // 用户参与投票
    {
        "name": "用户参与投票",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "join_vote",
            "data": {
                "access_token":"授权码",
                "vote_sha1":"vote_sha1",
                "vote_option_index":"所投选项",
                "content":"附加说明"
            }
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            "data":{
                "vote":{
                    "vote_sha1":"",
                    "vote_option":"选项列表[选项1, 选项二]",
                    "vote_result":"选项对应的票数[1,10]",
                    "vote_count":"当前总票数",
                    "me_is_vote":"我是否参与了投票(0:未参与, 1:参与了)",
                    "me_vote_option":"我投的选项下标",
                    "end_time":"结束时间",
                    "is_end":"是否已经结束(0:未结束, 1:已结束)",
                }
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
        }
    },

    // 发布一条Status
    {
        "name": "发布一条Status",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "publish_status",
            "data": {
                "access_token":"授权码",
                "title":"",
                "content":"",
                "image_list":"[]",
                "type":"类型 0:微交流(讨论) 1:微评选(投票) 2:随手拍 3:一起玩 4:发现 5:二手",
                "vote":{
                    "vote_option":"[]选项列表[选项1, 选项二]",
                    "end_time":"结束时间(0:6小时后, 1:12小时后, 2:1天后, 3:3天后, 4:7天后)"
                }
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "create_user":{
                    "user_sha1":"user_sha1",
                    "nick":"昵称",
                    "photo":"头像url",
                },
                "status_id":"",
                "status_sha1":"Status_sha1",
                "title":"标题",
                "content":"详细内容",
                "image_list":"图片url_list[http://XXX.com/XXX.png,...]",
                "type":"类型 0:讨论 1:投票 2:易物 3:发现",
                "create_time":"创建时间(2016-02-27 18:21:34)",
                "like_count":"点赞数",
                "share_count":"分享数",
                "comment_conut":"评论数",
                "vote":{
                    "vote_sha1":"选项列表[选项1, 选项二]",
                    "vote_result":"选项对应的票数[1,10]",
                    "vote_count":"当前总票数",
                    "me_is_vote":"我是否参与了投票(0:未参与, 1:参与了)",
                    "me_vote_option":"我投的选项下标",
                    "end_time":"结束时间",
                    "is_end":"是否已经结束(0:未结束, 1:已结束)",
                }
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 发布一条评论
    {
        "name": "发布一条评论",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "publish_comment",
            "data": {
                "access_token":"授权码",
                "content":"",
                "comment_sha1":"可选,如果回复别人的评论则需要",
                "status_sha1":"status_sha1",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "comment":{
                    "create_user":{
                        "user_sha1":"user_sha1",
                        "nick":"昵称",
                        "photo":"头像url",
                    },
                    "comment_id":"",
                    "comment_sha1":"Status_sha1",
                    "content":"评论内容",
                    "create_time":"创建时间(2016-02-27 18:21:34)",
                    "is_sub":"是否为子评论(0:不是 1:是)",
                    "other_user":{
                        "user_sha1":"user_sha1",
                        "nick":"昵称",
                        "photo":"头像url",
                    }
                },
                "like_count":"点赞数",
                "share_count":"分享数",
                "comment_conut":"评论数",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 点赞/取消点赞
    {
        "name": "点赞",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "click_like",
            "data": {
                "access_token":"授权码",
                "status_sha1":"status_sha1",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "like_count":"点赞数",
                "share_count":"分享数",
                "comment_conut":"评论数",
                "me_is_like":"我是否点过赞",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 分享
    {
        "name": "分享",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "share_count_add",
            "data": {
                "access_token":"授权码",
                "status_sha1":"status_sha1, 通过第三方分享,分享成功后调用此接口告诉服务器分享成功",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "like_count":"点赞数",
                "share_count":"分享数",
                "comment_conut":"评论数",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 删除一条Status
    {
        "name": "删除一条Status",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "delete_status",
            "data": {
                "access_token":"授权码",
                "status_sha1":"status_sha1",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 删除一条评论
    {
        "name": "删除一条评论",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "delete_comment",
            "data": {
                "access_token":"授权码",
                "comment_sha1":"comment_sha1",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 关注
    {
        "name": "关注",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "follow",
            "data": {
                "access_token":"授权码",
                "user_sha1":"要关注的用户的sha1",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 取消关注
    {
        "name": "取消关注",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "remove_follow",
            "data": {
                "access_token":"授权码",
                "user_sha1":"要取消关注的用户的sha1",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 更新头像
    {
        "name": "更新头像",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "update_photo",
            "data": {
                "access_token":"授权码",
                "photo":"头像url",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 更新个人页面背景图片
    {
        "name": "更新个人页面背景图片",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "update_profile_back",
            "data": {
                "access_token":"授权码",
                "photo":"图片url",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 更新用户标签
    {
        "name": "更新用户标签",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "update_tag_list",
            "data": {
                "access_token":"授权码",
                "tag_list":"[Python, IOS]",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 更新用户密码
    {
        "name": "更新用户密码",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "update_pwd",
            "data": {
                "access_token":"授权码",
                "old_pwd":"旧密码(MD5加密后上传)",
                "new_pwd":"新密码(MD5加密后上传)",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    //更新用户简介
    {
        "name": "更新用户简介",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "update_intro",
            "data": {
                "access_token":"授权码",
                "intro":"个人简介",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 更新用户资料
    {
        "name": "更新用户资料",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "update_info",
            "data": {
                "access_token":"授权码",
                "nick":"昵称",
                "email":"邮箱",
                "sex":"性别(0/1)",
                "birthday":"生日(1999-12-23)",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "个人详细信息":""
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 获取用户关注列表
    {
        "name": "获取用户关注列表",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "follow_user_list",
            "data": {
                "access_token":"授权码",
                "max_id":"获取follow_id < max_id的最新数据,可选,默认返回最新",
                "count":"可选,最大不超过50,默认返回20条",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "user_list":[
                    {
                        "follow_id":"",
                        "user_sha1":"user_sha1",
                        "nick":"昵称",
                        "photo":"头像url",
                    }
                ],
                "total_count":"总关注数"
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 获取系统推荐用户列表
    {
        "name": "获取系统推荐用户列表",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "recommend_user_list",
            "data": {
                "access_token":"授权码",
                "max_id":"获取follow_id < max_id的最新数据,可选,默认返回最新",
                "count":"可选,最大不超过50,默认返回20条",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "user_list":[
                    {
                        "follow_id":"",
                        "user_sha1":"user_sha1",
                        "nick":"昵称",
                        "photo":"头像url",
                    }
                ],
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 搜索用户
    {
        "name": "搜索用户",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "search_user_list",
            "data": {
                "access_token":"授权码",
                "max_id":"获取user_id < max_id的最新数据,可选,默认返回最新",
                "count":"可选,最大不超过50,默认返回20条",
                "key":"搜索关键字(匹配nick)",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "user_list":[
                    {
                        "follow_id":"",
                        "user_sha1":"user_sha1",
                        "nick":"昵称",
                        "photo":"头像url",
                    }
                ],
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 获取其他用户资料
    {
        "name": "获取其他用户资料",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "get_other_user_info",
            "data": {
                "access_token":"授权码",
                "user_sha1":"",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "user_sha1":"用户sha1",
                "nick":"昵称",
                "phone":"手机号码",
                "photo":"头像url",
                "email":"邮箱",
                "age":"年(22)",
                "sex":"性别(男,女)",
                "intro":"个人简介",
                "birthday":"生日",
                "university":"学校",
                "tag_list":"标签列表[Python, IOS...](字符串)",
                "create_time":"注册时间(2016-02-27 18:25:30)",
                "last_active_time":"最后活动时间(2016-02-27 18:25:30)",
                "is_follow":"我是否关注了他(0:未关注, 1:关注了)",
                "follow_count" : "关注数",
                "fans_count" : "粉丝数",
                "status_count" : "状态数",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 获取自己资料
    {
        "name": "获取自己资料",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "get_user_info",
            "data": {
                "access_token":"授权码",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "user_sha1":"用户sha1",
                "nick":"昵称",
                "phone":"手机号码",
                "photo":"头像url",
                "email":"邮箱",
                "age":"年(22)",
                "sex":"性别(男,女)",
                "intro":"个人简介",
                "birthday":"生日",
                "university":"学校",
                "active_university":"当前活动学校",
                "tag_list":"标签列表[Python, IOS...](字符串)",
                "create_time":"注册时间(2016-02-27 18:25:30)",
                "last_active_time":"最后活动时间(2016-02-27 18:25:30)",
                "follow_count" : "关注数",
                "fans_count" : "粉丝数",
                "status_count" : "状态数",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 获取消息列表
    {
        "name": "获取消息列表",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "message_list",
            "data": {
                "access_token":"授权码",
                "max_id":"获取message_id < max_id的最新数据,可选,默认返回最新",
                "count":"可选,最大不超过50,默认返回20条",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
                "message_list":[
                    {
                        "other_user":{
                            "user_sha1":"user_sha1",
                            "nick":"昵称",
                            "photo":"头像url",
                        },
                        "message_id":"",
                        "message_sha1":"",
                        "content":"消息内容",
                        "type":"0 未读, 1 已读",
                    }
                ],
                "total_count":"总消息条数",
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 将消息设为已读
    {
        "name": "将消息设为已读",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "read_message",
            "data": {
                "access_token":"授权码",
                "message_sha1":"",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },

    // 删除消息
    {
        "name": "删除消息",
        "url": "/yeps/api/",
        "method": "POST",
        "params": {
            "action": "delete_message",
            "data": {
                "access_token":"授权码",
                "message_sha1":"",
            },
        },
        "response": {
            "info": "OK",
            "ret": "0001",
            'data':{
            }
        },
        "note": {
            "请求参数": "-------------",
            "返回参数": "-------------",
            "info": "OK",
            "ret": "0001",
            
        }
    },
]

