from django.contrib import admin
from .models import student_info
# Register your models here.

@admin.register(student_info)
class student_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'contact']

