from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length= 100)
    id = models.IntegerField(primary_key=True, unique=True)
    location = models.CharField(max_length=100)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    cost = models.IntegerField()

