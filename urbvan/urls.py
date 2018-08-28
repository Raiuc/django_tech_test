# coding: utf8
from django.contrib import admin
from django.urls import (include, path)

from rest_framework.authtoken import views
from rest_framework import routers

from apps.stations.urls import urlpatterns_v1_locations
from apps.lines.views import LineViewSet, RouteViewSet, UserViewSet, GroupViewSet
from apps.stations.views import LocationViewSet, StationViewSet


"""
Routers used to connect serialized API views to the URL conf.
"""
router = routers.DefaultRouter()
router.register(r'lines', LineViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'location', LocationViewSet)
router.register(r'station', StationViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),

    path('v1/locations/', include(urlpatterns_v1_locations)),

    # API URLs
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls',  namespace='rest_framework')),
    # path('rest-auth/', include('rest_auth.urls')),

]
