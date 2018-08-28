from django.contrib import admin
from .models import LineModel, RouteModel

# Model visualization/editting in Django admin
class LineModelAdmin(admin.ModelAdmin):
    fields = ['id', 'name', 'color']

class RouteModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'line', 'get_stations', 'direction', 'is_active']
    list_filter = ['id', 'line', 'direction', 'is_active']
    list_per_page = 500

    def get_stations(self, obj):
        return "\n".join([p.stations for p in obj.stations.all()])


admin.site.register(LineModel, LineModelAdmin)
admin.site.register(RouteModel, RouteModelAdmin)
