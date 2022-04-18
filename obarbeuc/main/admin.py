from django.contrib import admin
from .models import TodayLunch, MenuItem, CovidList
from account.models import Account
from reservation.models import Reservation

# Register your models here.
admin.site.register(TodayLunch)
admin.site.register(Reservation)
admin.site.register(MenuItem)
admin.site.register(Account)
admin.site.register(CovidList)