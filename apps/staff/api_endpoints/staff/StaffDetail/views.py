from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from apps.staff.models import Employee
from .serializers import StaffDetailSerializer
from apps.attendance.models import Attendance


class StaffDetailApiView(RetrieveAPIView):
    serializer_class = StaffDetailSerializer
    queryset = Employee.objects.all()
    lookup_field = "id"


__all__ = ["StaffDetailApiView"]
