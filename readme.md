### 从0开始搭建校园二手交易平台
---
#### 0. 环境准备

**查看conda虚拟环境**   
```
conda env list
```
**激活Django环境**
```
conda activate django_env
```

#### 1. 创建项目
**创建项目**
```
django-admin startproject campus_market
python manage.py runserver
```
**浏览器打开**
```
http://127.0.0.1:8000
```

#### 2. 创建App
**2.1 创建“商品模块”**
```
python manage.py startapp goods
```
**2.2 注册App**
修改 `settings.py`
```py
INSTALLED_APPS = [
    ...
    "goods",
]
```

#### 3. 写第一个页面
**3.1 写视图**
`goods/views.py`
```py
from django.http import HttpResponse

def index(request):
    return HttpResponse("校园二手交易平台")
```
**3.2 配置子路由**
新建文件 `goods/urls.py`
```py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
]
```
**3.3 接入总路由**
`campus_market/urls.py`
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ...
    path("goods/", include('goods.urls')), # 把请求“转交”给 goods.urls 去处理
]
```

**🔁 请求执行顺序**
假设访问：
```
http://127.0.0.1:8000/goods
```
① 先进入 总路由 `campus_market/urls.py`
```py
path("goods/", include('goods.urls'))
```
匹配成功（因为是 /goods/ ）,然后把剩余路径（空路径 ""）交给 goods.urls

② 进入 子路由 `goods/urls.py`
```py
path("", views.index)
```
匹配成功，执行 `views.index(request)`

**最终URL = 主路由路径 + 子路由路径**
```
include = 把URL分发给另一个urls.py继续匹配
```

#### 4. 创建数据库模型
**4.1 定义商品模型**
`goods/models.py`
```py
from django.db import models

class Good(models.Model): # class类比表
    name = models.CharField(max_length=100) # 属性类别字段
    price = models.FloatField()
    desc = models.TextField()

    def __str__(self):
        return self.name # 定义后台显示样式
```

**4.2 生成数据库**
```
python manage.py makemigrations
python manage.py migrate
```
```
makemigrations = 把“Python代码变化”记录下来，生成“变更方案” / 迁移文件
migrate = 在数据库里创建/修改表
```

#### 5. 后台管理
**5.1 注册模型**
```py
from django.contrib import admin
from .models import Good
# Register your models here.

admin.site.register(Good)
```

**5.2 创建管理员**
```
python manage.py createsuperuser
```

**Django自带的后台管理系统（非常强），不需要自己写CRUD**

#### 6. 展示商品列表
**6.1 修改视图**
`goods/views.py`
```py
from django.shortcuts import render
from .models import Good

# index函数名，对应urls.py中的views.index；request参数是Django自动传入的HTTP请求对象
# 当用户访问网页，Django调用这个函数
def index(request):
    # 获取数据
    # Good：定义的模型（数据库表）
    # objects：Django提供的“查询管理器” 
    # all()：查询所有数据
    goods = Good.objects.all() # 本质是从数据库里取出所有商品

    # render(...) ：Django提供的函数，用来加载HTML模板 + 填充数据 + 返回页面
    # 'index.html'：要渲染的模板文件
    # {'变量名': 数据}，把 goods 这个数据，交给模板使用
    return render(request, "index.html", {"goods": goods}) 
```

**6.2创建模板**
新建目录 `goods/templates`
`index.html`
```html
<h1>校园二手交易平台</h1>

{% for good in goods %}
    <div>
        <h3>{{ good.name }}</h3>
        <p>价格: {{ good.price }}</p>
        <p>{{ good.desc }}</p>
    </div>
{% endfor %}
```

```
{{ }}  → 变量
{% %}  → 逻辑
```

解释：`from django.shortcuts import render` 和 `from django.http import HttpResponse`
| 方法           | 类比            |
| ------------ | ------------- |
| HttpResponse | 直接发短信         |
| render       | 发一份排版好的Word文档 |

```py
from django.http import HttpResponse # 从 Django 的 HTTP 模块中，引入 HttpResponse

def index(request):
    return HttpResponse("Hello") # 直接返回一段字符串,相当于：服务器直接把文字丢给浏览器

from django.shortcuts import render # render是更高级的方式（推荐用这个）

def index(request):
    return render(request, 'index.html') # 返回一个HTML页面，自动实现加载模板、传数据、渲染页面等
```
---
#### 总结
**1️⃣ Django的本质**
```
URL → View → Model → Template
```
**2️⃣ ORM思想**
```
‌ORM（Object-Relational Mapping，对象关系映射）‌ 是一种编程技术，
用于在‌面向对象编程语言‌（如 Java、Python等）与‌关系型数据库‌（如 MySQL、PostgreSQL等）之间建立映射关系，
从而实现‌用操作对象的方式操作数据库‌，
而无需直接编写 SQL 语句。

操作数据库 = 写Python代码
```
**3️⃣ MVC变体（Django叫MTV）**
| Django   | 含义   |
| -------- | ---- |
| Model    | 数据   |
| Template | 页面   |
| View     | 控制逻辑 |
