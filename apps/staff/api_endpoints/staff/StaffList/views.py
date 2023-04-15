from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from .serializers import StaffListSerializer

from apps.staff.models import Employee


class StaffListApiView(ListAPIView):
    serializer_class = StaffListSerializer
    queryset = Employee.objects.all()

    filter_backends = [
        SearchFilter, OrderingFilter, DjangoFilterBackend
    ]
    search_fields = ["name", "surname"]
    ordering_fields = ("name", "surname")


__all__ = ["StaffListApiView"]
