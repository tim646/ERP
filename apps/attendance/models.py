from django.db import models

from apps.staff.models import Employee

CHOICES = [('LATE', 'LATE'),
           ('EARLY', 'EARLY'),
           ('ABSENT', 'ABSENT'),
           ('ON-TIME', 'ON-TIME'),
           ('DAY OFF', 'DAY OFF'),
           ]


# Create your models here.
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=CHOICES, max_length=100, default='ABSENT', blank=True, null=True)

    def __str__(self):
        return self.employee.name
