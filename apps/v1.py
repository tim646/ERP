from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("staff/", include("apps.staff.urls")),
    path("attendance/", include("apps.attendance.urls")),
    path("project/", include("apps.project.urls")),
    path("event/", include("apps.event.urls")),
    path("inventory/", include("apps.inventory.urls")),
]
