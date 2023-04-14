from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import StaffCreateSerializer
from apps.staff.models import Employee


class StaffCreateAPIView(CreateAPIView):
    serializer_class = StaffCreateSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]


__all__ = ["StaffCreateAPIView"]
