from django.urls import path
from goods.views.goods_views import goods_list, add_goods, goods_detail
from goods.views.user_views import user_login

urlpatterns = [
    path('', goods_list),
    path('login/', user_login),
    path('add/', add_goods),
    path('detail/<int:id>/', goods_detail),
]