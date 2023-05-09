from django.contrib import admin
from django.contrib.admin import TabularInline

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'complete']
    list_display_links = ['title']
