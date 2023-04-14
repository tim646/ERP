from rest_framework.serializers import ModelSerializer
from apps.staff.models import Employee
from rest_framework import serializers


class StaffListSerializer(ModelSerializer):
    position = serializers.CharField(source="position.name")

    class Meta:
        model = Employee
        fields = [
            "id",
            "name",
            "surname",
            "position",
            "is_intern",
            "salary",
        ]
