# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import Publisher


# Create your views here.

# 引导页函数
def welcome(request):
    return HttpResponse('欢迎大家来到波波老师的内涵社区')


#####【发布者模块】######
# 登录界面
def publisher_login(request):
    # return HttpResponse('login')

    # 安装模板
    return render(request, "publisher/login.html")


# 注册页面
def publisher_register(request):
    # 模板中发生提交事件以后要在下面的代码中处理
    if request.method == 'POST':
        # 一旦发生POST事件，则在这里处理
        # 接收前端提出的数据
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']
        sex = request.POST['sex']
        signature = request.POST['signature']
        # 处理前端提交的数据
        # 建模
        pub = Publisher(username=username, password=password, nickname=nickname, sex=sex, signature=signature)
        # 存入数据库
        pub.save()
        return HttpResponse("注册成功！")

    # 安装模板
    return render(request, "publisher/register.html")


#####[公用模块]#######
# ajax请求的响应
def ajax_response(request):
    username = request.POST['username']
    return HttpResponse(username)