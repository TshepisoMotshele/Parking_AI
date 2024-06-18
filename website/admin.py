from django.contrib import admin
from .models import User, ParkingSession

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'license_plate_number')

@admin.register(ParkingSession)
class ParkingSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time')
