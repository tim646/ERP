from django.contrib import admin

from apps.staff.models import Employee, Position

# Register your models here.
admin.site.register(Employee)
admin.site.register(Position)
