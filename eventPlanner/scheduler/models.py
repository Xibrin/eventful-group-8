from django.db import models
from rest_framework import serializers


# Create your models here.
class Event(models.Model):
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=20, default="0/0/00")
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)

