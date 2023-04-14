from rest_framework.serializers import ModelSerializer
from apps.event.models import Event


class EventUpdateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "address",
            "date",
            "time",
        ]