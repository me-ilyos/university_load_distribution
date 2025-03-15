from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "head", "created_at")
    search_fields = ("code", "name")
    list_filter = ("created_at",)
