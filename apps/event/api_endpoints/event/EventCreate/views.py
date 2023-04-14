from rest_framework.generics import CreateAPIView

from .serializers import EventCreateSerializer
from apps.event.models import Event


class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer


__all__ = ["EventCreateAPIView"]
