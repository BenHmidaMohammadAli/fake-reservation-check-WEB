from django.db import models
from authentication.models import Passenger
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
    route = models.CharField(max_length=200, null=True)
    flight_pic = models.ImageField(null = True, blank=True)  
    date_created = models.DateTimeField(auto_now_add= True, null=True)  
    def __str__(self) :
        return self.name 
    
class ReservationFlight(models.Model):
    passenger = models.OneToOneField(Passenger, null=True, on_delete=models.CASCADE)
    sales_channel = models.CharField(max_length=200, null =True , blank= True)
    flight = models.OneToOneField(Flight, null=True, on_delete=models.CASCADE)
    travel_duration = models.IntegerField(null = True, blank=True)
    extra_baggage = models.BooleanField(null = True, blank=True) 
    meal = models.BooleanField(null = True, blank=True) 
    preffered_seat = models.BooleanField(null = True, blank=True) 
    number_of_chair = models.IntegerField(null= True , blank= True )
    number_of_chairs_to_reserve = models.IntegerField(null = True, blank=True)
    trip_type = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200,null = True , blank= True )
    state = models.BooleanField(null = True, blank=True)
    def __str__(self) :
        return "Passenger "+ str(self.passenger.id) + " for the flight " + str(self.flight.id ) 
    
class ReservationFlightPredictions(models.Model):
    reservationFlight = models.OneToOneField(ReservationFlight, null=True, on_delete=models.CASCADE)
    complete = models.BooleanField(null = True, blank=True)

