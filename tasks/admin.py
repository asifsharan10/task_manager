from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'due_date', 'priority', 'completed']
    list_filter = ['priority', 'completed']
    search_fields = ['title', 'user__username']

admin.site.register(Task, TaskAdmin)
