from django.db import models

# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=100)  # 标题
    price = models.FloatField()               # 价格
    description = models.TextField()          # 描述
    created_at = models.DateTimeField(auto_now_add=True)  # 发布时间

    def __str__(self):
        return self.title