from django.contrib import admin
from .models import *

# admin.site.register(TODO)

@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'title', 'description', 'status'
    ]
    ordering = ('id',)
    search_fields = ('title',)
    list_per_page = 3

# admin.site.register(Employee)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'age', 'address', 'department'
    ]
    search_fields = ('name','department',)
    ordering = ('id',)