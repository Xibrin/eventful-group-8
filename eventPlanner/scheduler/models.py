
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True

class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False, unique=True)
    username = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    confirm_password = models.CharField(max_length=100, null=False, blank=True)
    city = models.CharField(max_length=100, null=True, blank=False)
    state = models.CharField(max_length=100, null=True, blank=False)
    music = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    visual = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    performing = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    film = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    lectures = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    fashion = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    food = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    festivals = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    charity = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    sports = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    nightlife = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    family = models.IntegerField(choices=zip(range(1, 10), range(1, 10)), blank=False)
    # objects = models.Manager()


class State(BaseModel):
    state = models.CharField(max_length=100, null=True, blank=False)
    # objects = models.Manager()

class Event(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=True)
    duration = models.DurationField(null=True)
    category = models.CharField(max_length=200, null=True)
    picture = models.URLField(max_length=300, null=False, default="")
    tickets = models.URLField(max_length=300, null=True, default="")
    cost = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, null=False)
    description = models.CharField(max_length=500, null=True)
    address1 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=False, blank=False, default="")
    state = models.CharField(max_length=100, null=False, blank=False, default="")
    country = models.CharField(max_length=100, null=False, blank=False, default="")
    zip = models.IntegerField(null=True)
    # objects = models.Manager()

    def __str__(self):
        return f"{self.name} starting at {self.start_time} costing {self.cost}, ending at {self.end_time}"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)