from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "get_head_name", "created_at")
    search_fields = ("code", "name")
    list_filter = ("created_at",)

    def get_head_name(self, obj):
        if obj.head:
            return obj.head.get_full_name()
        return "-"

    get_head_name.short_description = "Department Head"
