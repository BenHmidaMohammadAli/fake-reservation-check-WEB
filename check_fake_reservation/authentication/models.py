from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Passenger(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True) 
    email = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    profil_pic = models.ImageField(null = True, blank=True)  
    date_created = models.DateTimeField(auto_now_add= True, null=True)  
    def __str__(self) :
        return self.name 