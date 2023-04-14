from rest_framework.serializers import ModelSerializer
from apps.event.models import Event


class EventDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "address",
            "date",
            "time",
            "created_at",
            "updated_at",
        ]
