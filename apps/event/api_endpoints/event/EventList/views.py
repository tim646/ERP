from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from apps.event.models import Event
from .serializers import EventListSerializer


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


__all__ = ["EventListAPIView"]
