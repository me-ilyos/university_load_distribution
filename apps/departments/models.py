from django.db import models
from django.utils import timezone
from apps.users.models import User


class Department(models.Model):
    code = models.CharField(
        max_length=10,
        unique=True,
        help_text="Unique code for the department (e.g., CS, MATH)",
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    head = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="headed_departments",
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}" if self.name else self.code
