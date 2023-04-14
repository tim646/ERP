from django.urls import path
from .api_endpoints import inventory

app_name = 'inventory'


urlpatterns = [
    path('InventoryList', inventory.InventoryListApiView.as_view(), name='inventory'),
    path('InventoryCreate', inventory.InventoryCreateAPIView.as_view(), name='inventory_create'),
    path('InventoryDetail/<int:id>', inventory.InventoryDetailAPIView.as_view(), name='inventory_detail'),
    path('InventoryDelete/<int:id>', inventory.InventoryDeleteAPIView.as_view(), name='inventory_delete'),
    path('InventoryUpdate/<int:id>', inventory.InventoryUpdateAPIView.as_view(), name='inventory_update'),

]
