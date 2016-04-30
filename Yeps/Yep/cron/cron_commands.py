#coding:utf-8
from django.core.management import call_command

def create_tester():
    call_command('create_test_user', 10)

def publish_one():
    call_command('publish_one', 10)