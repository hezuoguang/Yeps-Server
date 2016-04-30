#coding:utf-8
from django.core.management.base import BaseCommand
from Yep.models import OneContent, User
from Yep import api_tools
import datetime, random

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            count = int(args[0])
            photo_host = "http://7xrlo2.com1.z0.glb.clouddn.com/"
            for i in range(count):
                tester_count = User.objects.filter(is_tester=1).count()
                if tester_count == 0:
                    return
                tester = User.objects.filter(is_tester=1)[random.randint(0, tester_count-1)]
                one_count = OneContent.objects.filter(status=0).count()
                if one_count == 0:
                    return
                one = OneContent.objects.filter(status=0)[random.randint(0, one_count-1)]
                image_url = str("%sone_%d.jpg" % (photo_host, one.count))
                type = random.randint(0, 5)
                if type == 1:
                    type = 0
                api_tools.publish_status(tester.access_token,one.title,one.content,[image_url],type)
                tester.last_active_time = datetime.datetime.now()
                tester.save()
                one.status = 1
                one.save()
                print("success --- " + tester.university)
        except Exception,e:
            print(e)