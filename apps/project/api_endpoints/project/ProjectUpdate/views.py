from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.project.models import Project

from .serializers import ProjectUpdateSerializer


class ProjectUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectUpdateSerializer
    queryset = Project.objects.all()
    lookup_field = 'id'
