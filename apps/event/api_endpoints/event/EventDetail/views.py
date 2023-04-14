from rest_framework.generics import RetrieveAPIView

from .serializers import EventDetailSerializer
from apps.event.models import Event


class EventDetailAPIView(RetrieveAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    lookup_field = "id"


__all__ = ["EventDetailAPIView"]
