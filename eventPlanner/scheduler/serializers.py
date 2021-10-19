from rest_framework import serializers
from . models import *

class EventSerializer(serializers.ModelSerializer):
    class RestAppSetUp:
        model = Event
        fields = ['location', 'date', 'start_time', 'end_time']
