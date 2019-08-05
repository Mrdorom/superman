# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

from  django.contrib.auth.models import User,Group
from rest_framework import viewsets
from  testApp.serializers import UserSerializer

# Create your views here.


def login(request):
    """
    登录
    :param request:
    :return:
    """
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error':'username or password error'})
    else:
        return render(request,'login.html')

def loginout(request):
    '''
    登出
    :param request:
    :return:
    '''
    auth.logout(request)
    return render(request,'login.html')


def home(request):
    '''
    home 页面
    :param request:
    :return:
    '''
    return render(request,"home.html")