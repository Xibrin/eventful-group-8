from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Event(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=True)
    category = models.CharField(max_length=200, null=True)
    picture = models.URLField(max_length=300, null=False, default="")
    tickets = models.URLField(max_length=300, null=False, default="")
    cost = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, null=False)
    description = models.CharField(max_length=500, null=True)
    address1 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=False, blank=False, default="")
    state = models.CharField(max_length=100, null=False, blank=False, default="")
    country = models.CharField(max_length=100, null=False, blank=False, default="")
    zip = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} starting at {self.start_time} costing {self.cost}"

    def __eq__(self, other):
        return self.name == other.name
