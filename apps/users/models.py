from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField




# Create your models here.


class CustomUser(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Name',
    )
    surname = models.CharField(
        max_length=50, verbose_name='Surname',
    )
    patronymic = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Patronymic',
    )

    phone_number = PhoneNumberField(region='UZ', unique=True, verbose_name='Phone number')
    email = models.EmailField(
        max_length=255, blank=True, null=True, verbose_name='Email',
    )

    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name='Date created',
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name
