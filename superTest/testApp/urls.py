# coding:utf-8

#  Author='Dorom'

from django.conf.urls import url
from testApp.api import user

urlpatterns = [

	url(r'user/login', user.obtain_auth_token),
]


