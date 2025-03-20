# apps/professors/views.py
from rest_framework import viewsets
from .models import Professor
from .serializers import ProfessorSerializer, ProfessorListSerializer
from apps.users.permissions import IsAdmin, IsAdminOrDepartmentHead, IsProfessor


class ProfessorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for professors
    """

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    
    def get_serializer_class(self):
        if self.action == "list":
            return ProfessorListSerializer
        return ProfessorSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsAdmin]
        elif self.action in ["list"]:
            self.permission_classes = [IsAdminOrDepartmentHead]
        else:
            self.permission_classes = [IsAdminOrDepartmentHead | IsProfessor]
        return super().get_permissions()

    def get_queryset(self):
        queryset = Professor.objects.all()

        department_id = self.request.query_params.get("department")
        if department_id:
            queryset = queryset.filter(department_id=department_id)

        if self.request.user.role == "department_head":
            departments = self.request.user.headed_departments.all()
            queryset = queryset.filter(department__in=departments)

        elif self.request.user.role == "professor":
            queryset = queryset.filter(user=self.request.user)

        return queryset
