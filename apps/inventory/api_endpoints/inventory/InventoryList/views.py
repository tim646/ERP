from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import InventoryListSerializer
from apps.inventory.models import Inventory


class InventoryListApiView(ListAPIView):
    serializer_class = InventoryListSerializer
    queryset = Inventory.objects.all()
    filter_backends = [
        SearchFilter, OrderingFilter, DjangoFilterBackend
    ]
    search_fields = ["name", "purchased_date"]
    ordering_fields = ("price", "name", "purchased_date")


__all__ = ["InventoryListApiView"]
