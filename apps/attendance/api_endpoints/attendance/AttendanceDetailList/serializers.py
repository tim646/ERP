from datetime import datetime, time

from rest_framework.serializers import ModelSerializer
from apps.attendance.models import Attendance
from rest_framework import serializers


class AttendanceDetailListSerializer(ModelSerializer):
    late_minutes = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = [
            'date',
            'time',
            'status',
            'late_minutes',
        ]

    def get_late_minutes(self, obj):
        expected_arrival_time = time(hour=10, minute=0)
        actual_arrival_time = datetime.strptime(obj.time.strftime('%H:%M'), '%H:%M').time()
        if actual_arrival_time > expected_arrival_time:
            td = datetime.combine(obj.date, actual_arrival_time) - datetime.combine(obj.date, expected_arrival_time)
            late_minutes = td.seconds // 60
            return late_minutes
        return 0
