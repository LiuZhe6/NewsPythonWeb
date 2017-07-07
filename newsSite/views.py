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
    if request.method == 'POST':
        # 接收登录界面表单的数据
        username = request.POST['username']
        password = request.POST['password']

        # 根据数据，从数据库中查找用户
        users = Publisher.objects.filter(username=username)
        if users:
            # 说明用户名正确，进一步比较密码是否正确
            # 从userArray列表中取出一个元素
            user = users[0]
            if user.password == password:
                # 说明密码正确,登陆成功，就可以安装登录成功以后的模板

                # 将当前查询到的对象转成字典
                userDict = {'id': user.id,
                            'username': user.username,
                            'nickname': user.nickname,
                            'sex': user.sex,
                            'signature': user.signature}

                # 构建一个模板的上下文
                context = {}
                context['userinfo'] = userDict

                return render(request, 'publisher/index.html', context)

            else:
                # 说明密码不正确，直接给前端返回响应密码错误
                return HttpResponse('密码错误!')

        else:
            # 说明用户名不正确，返回 该用户不存在，直接给前端响应用户名不存在
            return HttpResponse('用户名不存在!')

            pass
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
        return HttpResponse("<script type='text/javascript>"
                            "alert('注册成功');"
                            "window.history.back();"
                            "</script>")

    # 安装模板
    return render(request, "publisher/register.html")


# 修改个人信息
def alter_info(request):
    if (request.method == 'POST'):
        if (request.POST['flag'] == 'index'):
            # 安装修改个人信息的模板
            userid = request.POST['userid']
            # 根据userid查找出对象
            userArr = Publisher.objects.filter(id=userid)
            user = userArr[0]

            # 转成字典
            user_dict = {'id': user.id,
                        'nickname': user.nickname,
                        'signature': user.signature,
                        'password': user.password}
            context = {'userinfo': user_dict}
            return render(request, 'publisher/alterinfo.html', context)
        else:
            # 说明不是index页面发出的请求，有可能是其他页面，处理模板的post请求
            user_id = request.POST['userid']
            userArr = Publisher.objects.filter(id=user_id)
            user = userArr[0]
            user.nickname = request.POST['nickname']
            user.signature = request.POST['signature']
            user.save()
            return HttpResponse("待添加修改模板")
            pass
    pass


# 发布新闻
def publish_news(request):
    return HttpResponse('发布模板待安装...')


#####[公用模块]#######
# ajax请求的响应
def ajax_response(request):
    username = request.POST['username']
    # 查询前端传过来的用户名是否在数据库中
    res = Publisher.objects.filter(username=username)
    # 将查询的结果作为响应体返回
    return HttpResponse(res)
