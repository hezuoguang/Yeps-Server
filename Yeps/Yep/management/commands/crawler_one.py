#coding:utf-8
from django.core.management.base import BaseCommand
from Yep.models import OneContent
import pyquery

class Command(BaseCommand):
    def getContent(self, count):
        max_one = OneContent.objects.order_by('-count').first()
        start = 0
        if max_one:
            start = max_one.count
        for i in range(count):
            index = i + start + 1
            p = pyquery.PyQuery("http://caodan.org/"+str(index)+"-photo.html")
            title = p(".entry-title").text()
            content = p("blockquote").find("p").eq(0).text()
            if len(title) <= 0 or len(content) <= 0:
                continue
            # titles = title.split(' ', 1)
            # if len(titles) > 1:
            #     title = titles[1]
            # else:
            #     title = titles[0]
            content = content + u" -- 转自「ONE · 一个」"
            one = OneContent()
            one.count = index
            one.title = title
            one.content = content
            try:
                one.save()
                print("success one" + str(index))
            except Exception,e:
                print("error one" + str(index))
                print(e)
    def handle(self, *args, **options):
        try:
            count = int(args[0])
            self.getContent(count)
        except Exception,e:
            print(e)