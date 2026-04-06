from django.shortcuts import render
from .models import Goods

# Create your views here.
def goods_list(request):
    goods = Goods.objects.all()
    return render(request, 'goods_list.html', {'goods': goods})