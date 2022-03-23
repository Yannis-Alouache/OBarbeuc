from django.db import models

# Create your models here.
class Reservation(models.Model):
    SERVICE_CHOICE = [
        ("Midi", "Midi"),
        ("Soir","Soir")
    ]
    lastName = models.CharField(max_length=50, blank=False, null=False)
    firstName = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=False, null=False)
    date = models.DateField(max_length=50, blank=False, null=False)
    table = models.IntegerField(blank=False, null=False, default=0)
    tableSetNumber = models.IntegerField(blank=False, null=False)
    service = models.CharField(blank=False, null=False, max_length=4, choices=SERVICE_CHOICE, default="Midi")

    def __str__(self):
        return "Reservation de " + self.lastName + " " + self.firstName + " le " + str(self.date)