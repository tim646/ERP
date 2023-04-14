from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.project.api_endpoints.project.ProjectCreate.serializers import ProjectCreateSerializer
from apps.project.models import Project


class ProjectDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    lookup_field = 'id'
