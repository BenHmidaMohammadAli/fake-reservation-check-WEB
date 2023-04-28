from django.db import models

# Create your models here.

class Flight(models.Model):

    flight_name = models.CharField(max_length=200, null=True)
    flight_UID = models.CharField(max_length=200, null=True)
    flight_duration = models.FloatField(null=True)
    flight_start = models.DateTimeField(null=True)
    flight_end = models.DateTimeField(null=True) 
    From = models.CharField(max_length=200, null=True)
    To = models.CharField(max_length=200, null=True)
    available = models.BooleanField(null = True, blank=True)  
    flight_pic = models.ImageField(null = True, blank=True)  
    date_created = models.DateTimeField(auto_now_add= True, null=True)  
    def __str__(self) :
        return self.name 