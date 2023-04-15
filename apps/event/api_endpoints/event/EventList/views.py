from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from apps.event.models import Event
from rest_framework import filters
from .serializers import EventListSerializer


class EventListAPIView(ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        "title",
    ]
    ordering_fields = ('date', 'title')


__all__ = ["EventListAPIView"]
