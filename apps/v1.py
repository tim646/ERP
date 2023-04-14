from django.urls import path, include

urlpatterns = [
    path("staff/", include("apps.staff.urls")),
    path("attendance/", include("apps.attendance.urls")),
    path("project/", include("apps.project.urls")),
    path("event/", include("apps.event.urls")),
    path("inventory/", include("apps.inventory.urls")),
]
