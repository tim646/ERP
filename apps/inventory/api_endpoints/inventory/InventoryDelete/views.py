from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.inventory.api_endpoints.inventory.InventoryDetail.serializers import InventoryDetailSerializer
from apps.inventory.models import Inventory


class InventoryDeleteAPIView(DestroyAPIView):
    serializer_class = InventoryDetailSerializer
    queryset = Inventory.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


__all__ = ["InventoryDeleteAPIView"]
