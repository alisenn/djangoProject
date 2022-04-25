
from django.db import models

# Create your models here.


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(
        'Vehicle',
        on_delete=models.CASCADE
    )
    datetime = models.DateTimeField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)


class Vehicle(models.Model):
    plate = models.CharField(max_length=20)