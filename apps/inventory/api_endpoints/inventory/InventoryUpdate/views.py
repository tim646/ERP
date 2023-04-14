from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.inventory.api_endpoints.inventory.InventoryCreate.serializers import InventoryCreateSerializer
from apps.inventory.models import Inventory


class InventoryUpdateAPIView(UpdateAPIView):
    serializer_class = InventoryCreateSerializer
    queryset = Inventory.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
