from rest_framework.generics import ListAPIView

from .serializers import InventoryListSerializer
from apps.inventory.models import Inventory


class InventoryListApiView(ListAPIView):
    serializer_class = InventoryListSerializer
    queryset = Inventory.objects.all()


__all__ = ["InventoryListApiView"]
