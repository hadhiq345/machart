from django.db import models

# Create your models here.\
class Location(models.Model):
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    places = models.JSONField()
    