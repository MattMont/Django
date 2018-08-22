from django.db import models
from django.urls import reverse

# Create your models here.
class Homeinfo(models.Model):
    address = models.CharField(max_length=150)
    estimate = models.IntegerField()
    neighbourhood = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    city = models.CharField(max_length=50, default='Edmonton')
    province = models.CharField(max_length=30, default='Alberta')
    country = models.CharField(max_length=100, default='Canada')


    def get_absolute_url(self):
        return reverse('sView', kwargs={'id': str(self.id)})
        #return reverse('hView', kwargs={'id': str(self.id)})
    def __str__(self):
        return self.address + ", " + self.city + ", " + self.province + ", " + self.country



class Listing(models.Model):
    image = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    realtor = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    bedrooms = models.IntegerField()
    bathrooms = models.FloatField()
    post_date = models.DateTimeField('date posted')
    def __str__(self):
        return self.address
