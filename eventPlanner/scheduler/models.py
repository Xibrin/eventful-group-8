from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    confirm_password = models.CharField(max_length=100, null=False, blank=False, default="0")
    music = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    visual = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    performing = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    film = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    lectures = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    fashion = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    food = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    festivals = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    charity = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    sports = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    nightlife = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    family = models.PositiveIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(10)])

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
