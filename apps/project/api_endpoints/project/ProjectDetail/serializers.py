from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.project.models import Project


class ProjectRetrieveSerializer(ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    project_type = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'category',
            'project_type',
            'start_date',
            'end_date',
            'is_finished',
        ]
