from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import TodayLunch, Reservation

# Register your models here.
admin.site.register(TodayLunch)
admin.site.register(Reservation)