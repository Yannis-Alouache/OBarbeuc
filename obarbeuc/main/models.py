from django.db import models

class TodayLunch(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)