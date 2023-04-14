from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.staff.models import Employee, Position


class StaffCreateSerializer(ModelSerializer):
    # position = serializers.IntegerField()
    class Meta:
        model = Employee
        fields = [
            "name",
            "surname",
            "patronymic",
            "email",
            "phone_number",
            "address",
            "salary",
            "position",
            "is_intern",
            "bio",
        ]
