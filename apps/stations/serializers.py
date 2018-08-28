from django.contrib.auth.models import User, Group

from rest_framework import serializers
from .models.locations import LocationModel
from .models.stations import StationModel


# Classes for API representation

# Serializer for lines
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Lines.
    """
    class Meta:
        model   = LocationModel
        fields  = ('id', 'name', 'latitude', 'longitude')

# Serializer for routes
class StationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Routes.
    """
    location   = LocationSerializer(many=False)

    class Meta:
        model   = StationModel
        fields  = ('id', 'location', 'order', 'is_active')
