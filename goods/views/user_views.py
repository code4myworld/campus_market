from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# 新增：登录功能
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/goods/')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

    return render(request, 'login.html')
