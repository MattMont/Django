from django.db import models
from django.urls import reverse

# Create your models here.
class Homeinfo(models.Model):
    address = models.CharField(max_length=100)
    estimate = models.IntegerField()
    neighbourhood = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('sView', kwargs={'id': str(self.id)})
        #return reverse('hView', kwargs={'id': str(self.id)})
    def __str__(self):
        return self.address
