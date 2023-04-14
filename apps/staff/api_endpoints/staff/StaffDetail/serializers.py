from rest_framework.serializers import ModelSerializer
from apps.staff.models import Employee
from rest_framework import serializers
from apps.attendance.api_endpoints.attendance.AttendanceDetailList.serializers import AttendanceDetailListSerializer


class StaffDetailSerializer(ModelSerializer):
    attendance = serializers.SerializerMethodField()
    position = serializers.CharField(read_only=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "name",
            "surname",
            "position",
            "bio",
            "is_intern",
            "salary",
            "attendance",
        ]

    def get_attendance(self, obj):
        attendance = obj.attendance_set.all()
        return AttendanceDetailListSerializer(attendance, many=True).data

    def position_set(self, obj):
        position = obj.position.name
        return position
