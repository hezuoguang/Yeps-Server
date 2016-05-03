#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from Yep.db_tools import share_status_detail, share_comment_list
# Create your views here.

def share_view(request):
    try:
        sha1 = request.GET['sha1']
        context = {}
        context['status'] = share_status_detail(sha1)
        context['comment_list'] = share_comment_list(sha1)
        type_info = [u'微交流',u'微评选',u'随手拍',u'一起玩',u'爱分享',u'二手']
        context['status']['type_info'] = type_info[context['status']['type']]
        if context['status']['type'] == 1:#投票
            context['vote_list'] = []
            total = context['status']['vote']['vote_count']
            for i in range(len(context['status']['vote']['vote_option'])):
                tmp = {}
                print(i)
                tmp['title'] = context['status']['vote']['vote_option'][i]
                tmp['count'] = context['status']['vote']['vote_result'][i]
                tmp['total'] = total
                tmp['pe'] = 1
                if total != 0:
                    tmp['pe'] = 1 + (tmp['count'] * 1.0 / total * 100.0)
                context['vote_list'].append(tmp)
        return render_to_response('yep/status_detail.html', context)
    except Exception,e:
        print(e)
        return render_to_response('yep/error.html',{})
