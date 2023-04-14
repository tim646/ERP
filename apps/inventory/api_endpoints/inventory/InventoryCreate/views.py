from rest_framework.generics import CreateAPIView
from apps.inventory.models import Inventory
from .serializers import InventoryCreateSerializer
from rest_framework.permissions import IsAuthenticated


class InventoryCreateAPIView(CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryCreateSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["InventoryCreateAPIView"]
