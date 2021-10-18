from django.db import models
from rest_framework import serializers

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    cost = models.IntegerField()

    def serializer(self):
        return {    
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "startTime": self.start_time,
            "endTime": self.end_time,
            "cost": self.cost
        }

