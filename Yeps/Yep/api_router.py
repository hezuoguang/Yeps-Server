#coding:utf-8
import  pdb,json,datetime,hashlib,time
from django.http import HttpResponse

from Yep.response_status import Status
from Yep import api_tools, tools
from Yep.api_tools import init_response_result


class ManageApi:
    # 获取系统用户标签列表
    def system_user_tag_list(self, request, params):
        result = init_response_result()
        result["data"]["tag_list"] = api_tools.system_user_tag_list()
        return result

    # 获取热门大学列表
    def active_university_list(self, request, params):
        result = init_response_result()
        result["data"]["university_list"] = api_tools.active_university_list()
        return result

    # 获取所有大学列表
    def system_university_list(self, request, params):
        result = init_response_result()
        result["data"]["university_list"] = api_tools.system_university_list()
        return result

    # 获取七牛token
    def qiniu_token(self, request, params):
        result = init_response_result()
        try:
            pic_name = params['pic_name']
            result = api_tools.qiniu_token(pic_name)
        except Exception,e:
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 检查手机号是否被注册
    def check_phone(self, request, params):
        result = init_response_result()
        try:
            phone = params['phone']
            result = api_tools.check_phone(phone)
        except Exception,e:
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 注册
    def register(self, request, params):
        result = init_response_result()
        try:
            phone = params['phone']
            nick = params['nick']
            pwd = params['pwd']
            photo = params['photo']
            sex = int(params['sex'])
            if sex < 0 or sex > 1:
                sex = 0
            tag_list = params['tag_list']
            university = params['university']
            if not tools.check_user_tag(tag_list) or not tools.check_school(university):
                raise ValueError
            result = api_tools.register(nick, phone, pwd, photo, sex, tag_list, university)
        except Exception,e:
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 登录
    def login(self, request, params):
        result = init_response_result()
        try:
            phone = params['phone']
            pwd = params['pwd']
            result = api_tools.login(phone, pwd)
        except Exception,e:
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 切换用户当前活动大学
    def switch_active_university(self, request, params):
        result = init_response_result()
        try:
            university = params['university']
            access_token = params['access_token']
            if not tools.check_school(university):
                raise ValueError
            result = api_tools.switch_active_university(access_token, university)
        except Exception,e:
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 获取Status 列表(讨论,投票,易物,发现)
    def status_list(self, request, params):
        result = init_response_result()
        try:
            access_token = params['access_token']
            since_id = params.get("since_id", -1)
            max_id = params.get("max_id", -1)
            type = params.get('type', -1)
            count = params.get('count', 20)
            is_follow = params.get('is_follow', 0)
            result["data"]['status_list'] = api_tools.status_list(access_token, since_id, max_id, type, count, is_follow)
        except Exception,e:
            print(e)
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 获取评论列表
    def comment_list(self, request, params):
        result = init_response_result()
        try:
            access_token = params['access_token']
            status_sha1 = params['status_sha1']
            max_id = params.get("max_id", -1)
            result["data"]['comment_list'] = api_tools.comment_list(access_token, status_sha1, max_id)
        except Exception,e:
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 获取Status评论数,点赞数,分享数
    def status_count(self, request, params):
        result = init_response_result()
        try:
            access_token = params['access_token']
            status_sha1 = params['status_sha1']
            result["data"] = api_tools.status_count(access_token, status_sha1)
        except Exception,e:
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 用户参与投票
    def join_vote(self, request, params):
        result = init_response_result()
        try:
            access_token = params['access_token']
            vote_sha1 = params['vote_sha1']
            vote_option_index = (int)(params['vote_option_index'])
            if vote_option_index < 0:
                raise ValueError
            content = params.get('content', '')
            result["data"]["vote"] = api_tools.join_vote(access_token, vote_sha1, vote_option_index, content)
        except Exception,e:
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 发布一条Status
    def publish_status(self, request, params):
        result = init_response_result()
        try:
            access_token = params['access_token']
            title = params['title']
            content = params['content']
            image_list = params.get('image_list', [])
            type = int(params['type'])
            if type < 0:
                raise ValueError
            if type == 1:
                vote_option = params['vote_option']
                end_time = params.get('end_time', 3)
            else:
                vote_option = []
                end_time = 3
            result["data"] = api_tools.publish_status(access_token, title, content, image_list, type, vote_option, end_time)
        except Exception,e:
            result["ret"] = Status.REQUESTPARAMSERROR
            result["info"] = Status().getReason(result["ret"])
            return result
        return result

    # 发布一条评论
    def publish_comment(self, request, params):
        result = init_response_result()
        return result

    # 点赞/取消点赞
    def click_like(self, request, params):
        result = init_response_result()
        return result

    # 分享
    def share_count_add(self, request, params):
        result = init_response_result()
        return result

    # 删除一条Status
    def delete_status(self, request, params):
        result = init_response_result()
        return result

    # 删除一条评论
    def delete_comment(self, request, params):
        result = init_response_result()
        return result

    # 关注
    def follow(self, request, params):
        result = init_response_result()
        return result

    # 取消关注
    def remove_follow(self, request, params):
        result = init_response_result()
        return result

    # 更新头像
    def update_photo(self, request, params):
        result = init_response_result()
        return result

    # 更新用户标签
    def update_tag_list(self, request, params):
        result = init_response_result()
        return result

    # 更新用户密码
    def update_pwd(self, request, params):
        result = init_response_result()
        return result

    # 更新用户简介
    def update_intro(self, request, params):
        result = init_response_result()
        return result

    # 更新用户资料
    def update_info(self, request, params):
        result = init_response_result()
        return result

    # 获取用户关注列表
    def follow_user_list(self, request, params):
        result = init_response_result()
        return result

    # 获取系统推荐用户列表
    def recommend_user_list(self, request, params):
        result = init_response_result()
        return result

    # 搜索用户
    def search_user_list(self, request, params):
        result = init_response_result()
        return result

    # 获取其他用户资料
    def get_other_user_info(self, request, params):
        result = init_response_result()
        return result

    # 获取自己资料
    def get_user_info(self, request, params):
        result = init_response_result()
        return result

    # 获取消息列表
    def message_list(self, request, params):
        result = init_response_result()
        return result

    # 将消息设为已读
    def read_message(self, request, params):
        result = init_response_result()
        return result

    # 删除消息
    def delete_message(self, request, params):
        result = init_response_result()
        return result

manage_api = ManageApi()
# api路由
def api_router(request):
    result = {}
    try:
        if request.method == 'POST':
            func_name = request.POST["action"]
            params = json.loads(request.POST["data"]) if request.POST.has_key("data") else {}
            result = getattr(manage_api, func_name, None)(request, params)
        elif request.method == 'GET':
            func_name = request.GET["action"]
            if func_name != "get_token":
                result = init_response_result()
                result["ret"] = Status.REQUESTMETHODERROR
                result["info"] = Status().getReason(result["ret"])
            else:
                params = {}
                result = getattr(manage_api, func_name, None)(request, params)
        else:
            return HttpResponse(json.dumps({}))
    except Exception, e:
        print(e)
        result = init_response_result()
        result["ret"] = Status.REQUESTPARAMSERROR
        result["info"] = Status().getReason(result["ret"])

    if result.has_key('cookies'):
        cookies = result['cookies']
        del result['cookies']
        response = HttpResponse(json.dumps(result))
        for key, value in cookies.items():
            response.set_cookie(key, value)
    else:
        response = HttpResponse(json.dumps(result))

    return response
