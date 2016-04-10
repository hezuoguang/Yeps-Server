#coding=utf-8
admin_status = {
    '1111': '服务器繁忙',
    '1112': '请求方式错误,应使用POST',
    '1113': '请求参数错误',

    '0001': '正常',
    '0002': '手机号已被注册',
    '0003': '手机号或密码错误',

    '1001': '投票已结束',
    '1002': '您已投过票',

}

class Status:
    UNKNOWNERR                        = '1111'
    REQUESTMETHODERROR                = '1112'
    REQUESTPARAMSERROR                = '1113'

    OK                                = '0001'
    PHONEEXISTS                       = '0002'
    PHONEORPWDERROR                   = '0003'

    VOTEENDERRPOR                     = '1001'
    VOTEREPEATERRPOR                  = '1002'


    def getReason(self, code):
        return admin_status[code]