from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import EventCreateSerializer
from apps.event.models import Event


class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["EventCreateAPIView"]
