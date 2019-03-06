from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):

    用户 = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)  # 作者
    thing = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural="待办事项"