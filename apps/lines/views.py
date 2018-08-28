from django.contrib.auth.models import User, Group
from django.shortcuts import render

from rest_framework import viewsets

from .models import LineModel, RouteModel
from .serializers import UserSerializer, GroupSerializer, LineSerializer, RouteSerializer

# API View for Line model
class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allow view and edit lines.
    """
    queryset         = LineModel.objects.all()
    serializer_class = LineSerializer
    paginator        = None

    class Meta:
        ordering = ['-id']

# API View for Route model
class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allow view and edit routes.
    """
    queryset         = RouteModel.objects.all()
    serializer_class = RouteSerializer
    paginator        = None

    class Meta:
        ordering = ['-id']

# Django-auth User API View
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset         = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    paginator        = None

    class Meta:
        ordering = ['-id']

# Django-auth Group API View
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset         = Group.objects.all()
    serializer_class = GroupSerializer
    paginator        = None

    class Meta:
        ordering = ['-id']
