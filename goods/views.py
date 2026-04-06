from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Goods

# Create your views here.
def goods_list(request):
    goods = Goods.objects.all()
    return render(request, 'goods_list.html', {'goods': goods})

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

# “发布商品”视图
@login_required
def add_goods(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')

        Goods.objects.create(
            title=title,
            price=price,
            description=description,
            user=request.user
        )

        return redirect('/goods/')

    return render(request, 'add_goods.html')

# 商品详情页
def goods_detail(request, id):
    goods = Goods.objects.get(id=id)
    return render(request, 'goods_detail.html', {'goods': goods})