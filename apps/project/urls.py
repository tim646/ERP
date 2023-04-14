from django.urls import path
from .api_endpoints import project

app_name = 'project'

urlpatterns = [
    path('ProjectList', project.ProjectListAPIView.as_view(), name='project'),
    path('ProjectDetail/<int:id>', project.ProjectRetrieveAPIView.as_view(), name='project_detail'),
    path('ProjectUpdate/<int:id>', project.ProjectUpdateAPIView.as_view(), name='project_update'),
    path('ProjectCreate', project.ProjectCreateAPIView.as_view(), name='project_create'),
    path('ProjectDelete/<int:id>', project.ProjectDeleteAPIView.as_view(), name='project_delete'),
]
