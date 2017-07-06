# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# 引导页函数
def welcome(request):
    return HttpResponse('欢迎大家来到波波老师的内涵社区')


#########[发布者模块]#########
# 登录界面
def publisher_login(request):
    return render(request, "publisher/login.html")

def publisher_register(request):
    return render(request,"publisher/register.html")