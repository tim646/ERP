from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.project.models import Project, Category, ProjectType


class ProjectUpdateSerializer(ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    project_type = serializers.PrimaryKeyRelatedField(queryset=ProjectType.objects.all(), many=True)

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
