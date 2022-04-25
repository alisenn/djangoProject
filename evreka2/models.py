
from django.db import models

# Create your models here.


class Bin(models.Model):
    collection_frequency = models.IntegerField(default=0)
    last_collection = models.DateTimeField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)


class Operation(models.Model):
    name = models.CharField(max_length=100)