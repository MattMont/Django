from django.db import models

# Create your models here.
class Homeinfo(models.Model):
    address = models.CharField(max_length=100)
    estimate = models.IntegerField()
    neighbourhood = models.CharField(max_length=100, blank=True, null=True)

