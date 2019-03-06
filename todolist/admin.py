from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Todo

# Register your models here.

class TodoInline(admin.TabularInline):
    model = Todo
    can_delete = True
    verbose_name_plural = '待办事项'

class UserAdmin(BaseUserAdmin):
    inlines = (TodoInline,)



admin.site.unregister(User)
admin.site.register(User,UserAdmin)