from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.staff.models import Employee
from apps.staff.api_endpoints.staff.StaffDetail.serializers import StaffDetailSerializer


class StaffDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffDetailSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'


__all__ = ['StaffDeleteAPIView']
