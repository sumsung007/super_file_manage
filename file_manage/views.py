from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'file_manage/file_manage.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
		# code = request.POST.get('code')
		# session_code = request.session.get('code')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/file_manage/index')
        else:
            return render(request, 'login.html', {'msg':'用户名不存在或密码错误'})
    return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/file_manage/login")



def user_manage(request):
    if request.method == 'GET':
        return render(request, 'file_manage/user_manage.html')
