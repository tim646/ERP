from rest_framework.serializers import ModelSerializer
from apps.staff.models import Employee


class StaffCreateSerializer(ModelSerializer):
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
