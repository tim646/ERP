from rest_framework.serializers import ModelSerializer
from apps.inventory.models import Inventory


class InventoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            "id",
            "name",
            "description",
            "price",
            "quantity",
            'purchased_date',
            "created_at",
            "updated_at",

        ]
