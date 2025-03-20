from django.db import models
from django.utils import timezone
from apps.users.models import User
from apps.departments.models import Department


class Professor(models.Model):
    # Experience level choices
    EXPERIENCE_BEGINNER = "beginner"
    EXPERIENCE_INTERMEDIATE = "intermediate"
    EXPERIENCE_EXPERIENCED = "experienced"

    EXPERIENCE_CHOICES = [
        (EXPERIENCE_BEGINNER, "Beginner"),
        (EXPERIENCE_INTERMEDIATE, "Intermediate"),
        (EXPERIENCE_EXPERIENCED, "Experienced"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="professor_profile"
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="professors"
    )

    has_degree = models.BooleanField(
        default=False, help_text="Whether the professor has a doctoral degree"
    )
    employment_type = models.FloatField(
        default=1.0, help_text="1.0 for full-time, 0.5 for half-time, etc."
    )
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default=EXPERIENCE_BEGINNER,
        help_text="Professor's experience level for workload distribution weighting",
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["user__last_name", "user__first_name"]

    def __str__(self):
        return self.user.get_full_name() or self.user.email

    @property
    def max_hours(self):
        """Calculate maximum teaching hours based on employment type and degree status"""
        base_hours = 400 if self.has_degree else 300
        return int(base_hours * self.employment_type)

    @property
    def full_name(self):
        """Get the professor's full name"""
        return self.user.get_full_name()

    @property
    def email(self):
        """Get the professor's email"""
        return self.user.email

    @property
    def experience_weight(self):
        """
        Get numerical weight based on experience level for distribution algorithm
        Returns a value between 1-3 where 3 represents most experienced
        """
        weights = {
            self.EXPERIENCE_BEGINNER: 1,
            self.EXPERIENCE_INTERMEDIATE: 2,
            self.EXPERIENCE_EXPERIENCED: 3,
        }
        return weights.get(self.experience_level, 1)
