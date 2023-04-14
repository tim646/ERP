from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

from apps.staff.models import Employee
from .serializers import AttendanceSerializer


class AttendanceCreateAPIView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        employee = get_object_or_404(Employee, id=self.kwargs.get("employee_id"))
        serializer.save(employee=employee)


__all__ = ['AttendanceCreateAPIView']
