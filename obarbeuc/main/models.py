from operator import mod
from django.db import models
from account.models import Account

class TodayLunch(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)

class CovidList(models.Model):
    SERVICE_CHOICE = [
        ("Midi", "Midi"),
        ("Soir","Soir")
    ]

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField(max_length=50, blank=False, null=False)
    service = models.CharField(blank=False, null=False, max_length=4, choices=SERVICE_CHOICE, default="Midi")

    def __str__(self):
        return self.user.__str__() + " " + str(self.date)