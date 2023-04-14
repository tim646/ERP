from django.contrib import admin

from .models import Project, Category, ProjectType

# Register your models here.

admin.site.register(Category)
admin.site.register(ProjectType)
admin.site.register(Project)
