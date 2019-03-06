"""首页实现登录功能，使用Django自带的admin登录验证系统
"""

from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import HttpResponse, HttpResponseRedirect


#首页（登录页面）
def index(request):
    return render(request, 'index.html')


def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user) #登录
        response = HttpResponseRedirect("type")
        response.set_cookie('user', username, 3600)  # 向浏览器添加cookie
        return response
    else:
        return render(request, 'index.html', {'error': "用户名或者密码输入错误"})