from django.urls import path
from .views import goods_detail, goods_list, user_login, add_goods

urlpatterns = [
    path('', goods_list),
    path('login/', user_login),
    path('add/', add_goods),
    path('detail/<int:id>/', goods_detail),
]