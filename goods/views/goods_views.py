from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from goods.services.goods_service import create_goods, delete_goods 
from goods.models import Goods

def goods_list(request):
    goods = Goods.objects.all()
    return render(request, 'goods_list.html', {'goods': goods})

# 商品详情页
def goods_detail(request, id):
    goods = Goods.objects.get(id=id)
    return render(request, 'goods_detail.html', {'goods': goods})

# “发布商品”视图
@login_required
def add_goods(request):
    if request.method == 'POST':
        create_goods(request.user, request.POST, request.FILES) 

        return redirect('/goods/')

    return render(request, 'add_goods.html')

# “我的商品”视图
@login_required
def my_goods(request):
    goods = Goods.objects.filter(user=request.user)
    return render(request, 'my_goods.html', {'goods': goods})


# 删除商品视图
@login_required
def delete_goods_view(request, id):
    delete_goods(request.user, id)
    return redirect('/goods/my/')