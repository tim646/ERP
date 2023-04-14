from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import EventUpdateSerializer
from apps.event.models import Event


class EventUpdateAPIView(UpdateAPIView):
    serializer_class = EventUpdateSerializer
    queryset = Event.objects.all()
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


__all__ = ["EventUpdateAPIView"]
