from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

from apps.project.models import Project
from .serializers import ProjectCreateSerializer


class ProjectCreateAPIView(CreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


__all__ = ['ProjectCreateAPIView']
