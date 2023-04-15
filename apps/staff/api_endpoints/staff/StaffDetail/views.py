from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from apps.staff.models import Employee
from .serializers import StaffDetailSerializer


class StaffDetailApiView(RetrieveAPIView):
    serializer_class = StaffDetailSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


__all__ = ["StaffDetailApiView"]
