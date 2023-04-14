from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.event.models import Event


class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'title',
            'date',
            'time',
            'address',
        ]
