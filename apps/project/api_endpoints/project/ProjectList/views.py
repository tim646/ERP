from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.project.models import Project
from .serializers import ProjectListSerializer


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


__all__ = ["ProjectListAPIView"]
