from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ..EventDetail.serializers import EventDetailSerializer

from apps.event.models import Event


class EventDeleteAPIView(DestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
