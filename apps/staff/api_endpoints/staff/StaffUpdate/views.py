from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.staff.api_endpoints.staff.StaffCreate.serializers import StaffCreateSerializer

from apps.staff.models import Employee


class StaffUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffCreateSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'


__all__ = ['StaffUpdateAPIView']