from django.contrib import admin
from .models.locations import LocationModel
from .models.stations import StationModel

# Model visualization/editting in Django admin
class LocationModelAdmin(admin.ModelAdmin):
    list_filter = ['id', 'name', 'latitude', 'longitude']
    list_per_page = 500


class StationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'order', 'is_active']
    list_per_page = 500

admin.site.register(LocationModel, LocationModelAdmin)
admin.site.register(StationModel, StationModelAdmin)
