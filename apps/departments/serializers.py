from rest_framework import serializers
from .models import Department
from apps.users.serializers import UserSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    head_details = UserSerializer(source="head", read_only=True)

    class Meta:
        model = Department
        fields = [
            "id",
            "code",
            "name",
            "description",
            "head",
            "head_details",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class DepartmentListSerializer(serializers.ModelSerializer):
    head_name = serializers.CharField(source="head.get_full_name", read_only=True)

    class Meta:
        model = Department
        fields = ["id", "code", "name", "head_name"]
