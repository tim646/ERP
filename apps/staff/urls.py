from django.urls import path
from .api_endpoints import staff

app_name = 'staff'

urlpatterns = [
    path('StaffList', staff.StaffListApiView.as_view(), name='staff'),
    path('<int:id>/', staff.StaffDetailApiView.as_view(), name='staff_detail'),
    path('<int:id>/update/', staff.StaffUpdateAPIView.as_view(), name='staff_update'),
    path('<int:id>/delete/', staff.StaffDeleteAPIView.as_view(), name='staff_delete'),
    path('create/', staff.StaffCreateAPIView.as_view(), name='staff_create'),
]