from rest_framework.serializers import ModelSerializer
from apps.attendance.models import Attendance, CHOICES
from rest_framework import serializers
from datetime import datetime


class AttendanceSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=CHOICES, read_only=True)
    employee = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Attendance
        fields = [
            'employee',
            'date',
            'time',
            'status',
        ]

    def create(self, validated_data):
        date = validated_data['date']
        time = validated_data['time']

        if date.weekday() == 6:
            validated_data['status'] = 'DAY OFF'
        else:
            start_time = datetime.strptime('10:00 AM', '%I:%M %p').time()
            if time > start_time:
                validated_data['status'] = 'LATE'
            elif time < start_time:
                validated_data['status'] = 'EARLY'
            elif time is None:
                validated_data['status'] = 'ABSENT'
            else:
                validated_data['status'] = 'ON-TIME'

        # Create the attendance object with the validated data
        attendance = Attendance.objects.create(**validated_data)
        return attendance
