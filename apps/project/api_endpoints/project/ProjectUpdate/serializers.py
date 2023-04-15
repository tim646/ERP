from rest_framework.serializers import ModelSerializer

from apps.project.models import Project


class ProjectUpdateSerializer(ModelSerializer):
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
