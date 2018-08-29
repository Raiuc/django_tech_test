# coding: utf8
from django.db import models

from apps.stations.models import StationModel

from apps.utils import create_id

# Class to to define lines table
class LineModel(models.Model):
    # used to correct collisions due to unique IDs generated in migrations
    # id = models.AutoField(auto_created=True, primary_key=True,
    #                       max_length=30, unique=True)
    id = models.CharField(default=create_id('line_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

# Class to to define routes table
class RouteModel(models.Model):

    id = models.CharField(default=create_id('route_'), primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
