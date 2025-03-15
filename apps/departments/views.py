from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentSerializer, DepartmentListSerializer
from apps.users.permissions import IsAdmin, IsAdminOrDepartmentHead


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for departments
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return DepartmentListSerializer
        return DepartmentSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [IsAdminOrDepartmentHead]
        else:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()
