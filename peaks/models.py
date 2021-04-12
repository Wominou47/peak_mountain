from django.db import models

# Create your models here.
class Peak(models.Model):
    name = models.CharField(max_length=200,blank=False)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    alt = models.FloatField(default=0.0)