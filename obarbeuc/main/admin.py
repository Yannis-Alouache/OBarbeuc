from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import TodayLunch, Reservation, MenuItem
from account.models import Account

# Register your models here.
admin.site.register(TodayLunch)
admin.site.register(Reservation)
admin.site.register(MenuItem)
admin.site.register(Account)