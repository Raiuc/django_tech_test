from django.contrib.auth.models import User, Group

from rest_framework import serializers
from .models import LineModel, RouteModel

# Classes for API representation

# Serializer for lines
class LineSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Lines.
    """
    class Meta:
        model   = LineModel
        fields  = ('id', 'name', 'color')

# Serializer for routes
class RouteSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Routes.
    """
    line       = LineSerializer(many=False)

    class Meta:
        model   = RouteModel
        fields  = ('id', 'line', 'stations', 'direction', 'is_active')

# Serializer for users
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Users.
    """
    class Meta:
        model    = User
        fields   = ('url', 'username', 'email', 'groups')

# Serializer for groups
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Groups.
    """
    class Meta:
        model   = Group
        fields  = ('url', 'name')
