from rest_framework.generics import ListAPIView
from .serializers import StaffListSerializer

from apps.staff.models import Employee


class StaffListApiView(ListAPIView):
    serializer_class = StaffListSerializer
    queryset = Employee.objects.all()


__all__ = ["StaffListApiView"]
