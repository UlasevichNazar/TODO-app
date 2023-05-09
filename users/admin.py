from django.contrib import admin
from django.contrib.admin import TabularInline

from tasks.models import Task
from users.models import User


class UserTaskInline(TabularInline):
    model = Task
    fields = ['title', 'description']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    inlines = (UserTaskInline,)
