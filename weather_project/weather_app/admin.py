from django.contrib import admin
from .models import Weather

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature', 'condition', 'humidity', 'wind_speed', 'timestamp')
    list_filter = ('condition',)
    search_fields = ('city',)
