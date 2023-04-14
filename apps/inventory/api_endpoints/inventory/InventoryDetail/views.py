from rest_framework.generics import RetrieveAPIView
from apps.inventory.models import Inventory

from .serializers import InventoryDetailSerializer


class InventoryDetailAPIView(RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryDetailSerializer
    lookup_field = "id"


__all__ = ["InventoryDetailAPIView"]
