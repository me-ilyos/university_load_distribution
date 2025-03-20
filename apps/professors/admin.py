from django.contrib import admin
from .models import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "department",
        "has_degree",
        "employment_type",
        "experience_level",
        "max_hours",
    )
    list_filter = ("department", "has_degree", "employment_type", "experience_level")
    search_fields = ("user__first_name", "user__last_name", "user__email")
    readonly_fields = ("created_at", "updated_at", "max_hours")

    fieldsets = (
        (None, {"fields": ("user", "department")}),
        (
            "Qualifications",
            {"fields": ("has_degree", "experience_level")},
        ),
        ("Employment Details", {"fields": ("employment_type", "max_hours")}),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    def full_name(self, obj):
        return obj.full_name

    def email(self, obj):
        return obj.email
