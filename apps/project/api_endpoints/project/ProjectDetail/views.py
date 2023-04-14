from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from apps.project.models import Project

from .serializers import ProjectRetrieveSerializer


class ProjectRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectRetrieveSerializer
    queryset = Project.objects.all()
    lookup_field = 'id'


__all__ = ['ProjectRetrieveAPIView']
