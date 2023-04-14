from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    project_type = models.ManyToManyField(ProjectType)
    link = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name
