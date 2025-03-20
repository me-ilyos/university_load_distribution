from rest_framework import serializers
from apps.users.serializers import UserSerializer
from apps.departments.serializers import DepartmentSerializer
from .models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source="user", read_only=True)
    department_details = DepartmentSerializer(source="department", read_only=True)
    max_hours = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    experience_weight = serializers.IntegerField(read_only=True)

    class Meta:
        model = Professor
        fields = [
            "id",
            "user",
            "user_details",
            "department",
            "department_details",
            "specialties",
            "has_degree",
            "employment_type",
            "experience_level",
            "experience_weight",
            "max_hours",
            "full_name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ProfessorListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)
    department_name = serializers.CharField(source="department.name", read_only=True)
    max_hours = serializers.IntegerField(read_only=True)

    class Meta:
        model = Professor
        fields = [
            "id",
            "full_name",
            "department_name",
            "has_degree",
            "employment_type",
            "experience_level",
            "max_hours",
        ]
