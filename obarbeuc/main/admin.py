from django.contrib import admin
from .models import TodayLunch, Reservation

# Register your models here.
admin.site.register(TodayLunch)
admin.site.register(Reservation)
