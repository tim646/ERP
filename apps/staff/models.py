from django.db import models
from django.contrib.auth.models import User, AbstractUser
from apps.users.models import CustomUser


# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(CustomUser):
    address = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    is_intern = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    salary = models.DecimalField(max_digits=12, decimal_places=3)

    def __str__(self):
        return self.name
