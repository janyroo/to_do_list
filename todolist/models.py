from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):

    用户 = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)  # 作者
    thing = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    work_time = models.IntegerField(default=0)
    格式化秒 = models.CharField(max_length=15)
    class Meta:
        verbose_name_plural="待办事项"