from django.urls import path
from .api_endpoints import event

app_name = 'event'

urlpatterns = [
    path('EventList', event.EventListAPIView.as_view(), name='event'),
    path('EventDetail/<int:id>', event.EventDetailAPIView.as_view(), name='event_detail'),
    path('EventCreate', event.EventCreateAPIView.as_view(), name='event_create'),
    path('EventUpdate/<int:id>', event.EventUpdateAPIView.as_view(), name='event_update'),
    path('EventDelete/<int:id>', event.EventDeleteAPIView.as_view(), name='event_delete'),
]