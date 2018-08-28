from django.shortcuts import render

from rest_framework import viewsets

from .models.locations import LocationModel
from .models.stations import StationModel
from .serializers import LocationSerializer, StationSerializer

# API View for Location model
class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allow view and edit locations.
    """
    queryset         = LocationModel.objects.all()
    serializer_class = LocationSerializer
    paginator        = None

    class Meta:
        ordering = ['-id']

# API View for Station model
class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allow view and edit stations.
    """
    queryset         = StationModel.objects.all()
    serializer_class = StationSerializer
    paginator        = None

    class Meta:
        ordering = ['-id']
