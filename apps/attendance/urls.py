from django.urls import path
from .api_endpoints import attendance

app_name = 'attendance'

urlpatterns = [
    path('AttendanceCreate/<int:employee_id>', attendance.AttendanceCreateAPIView.as_view(), name='attendance_create'),
]

