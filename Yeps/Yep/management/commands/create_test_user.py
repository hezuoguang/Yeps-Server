#coding:utf-8
from django.core.management.base import BaseCommand,CommandError
import hashlib, random, datetime, json
from Yep.models import User
from Yep import api_tools
from Yep import pynamesgenerator

class Command(BaseCommand):
    def create_test_user(self, count):
        user_count = User.objects.all().count()
        phone = 60000000000 + user_count
        pwd = hashlib.new('md5', '123456').hexdigest()

        sex_list = ['男', '女', '女', '男', '女', '男', '女', '女', '男','女', '女']
        university_list = ['怀化学院', '湖南大学', '吉首大学', '华南理工大学']
        photo_host = "http://7xrlo2.com1.z0.glb.clouddn.com/"
        for i in range(0, count):
            cur_count = user_count + i
            tphone = str(phone + i)
            sex = sex_list[random.randint(0,len(sex_list) - 1)]
            university = university_list[random.randint(0,len(university_list)-1)]
            birthday = pynamesgenerator.my_gen_birthday()
            if sex == '男':
                nick = pynamesgenerator.gen_one_gender_word(male=True)
                photo = str("%sm-photo%d" % (photo_host, cur_count % 1985))
            else:
                nick = pynamesgenerator.gen_one_gender_word(male=False)
                photo = str("%sw-photo%d.jpeg" % (photo_host, cur_count % 3081))

            try:
                api_tools.register(nick, tphone, pwd, photo, sex, ['Python', 'IOS'], university)
                # db_tools.create_user(nick, tphone, pwd, photo, sex, ['Python', 'IOS'], university, birthday)
                user = User.objects.get(phone=tphone)
                date = datetime.datetime.now() - datetime.timedelta(hours=random.randint(2,27))
                user.last_active_time = date
                user.create_time = date
                image_list = [photo]
                user.image_list = json.dumps(image_list)
                user.is_tester = int(1)
                user.birthday = birthday
                user.save()
                print("success---" + tphone + "---" + sex)
            except Exception,e:
                print(e)
    def handle(self, *args, **options):
        try:
            try:
                count = int(args[0])
            except:
                count = 10
            self.create_test_user(count)
        except Exception,e:
            print(e)