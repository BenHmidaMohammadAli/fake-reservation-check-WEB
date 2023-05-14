from django.shortcuts import render
from .decorators import *
from authentication.models import Passenger
from .form import CreatePassengerForm  , CreateUserForm, CreateFlightForm , CreateFlightReservationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Flight ,ReservationFlight ,ReservationFlightPredictions
from .Model.model import model_predict
from datetime import datetime
import csv 

# Create your views here.


#@unauthenticated_user
def home_admin_reservation_dashboard (request):
    if request.user.is_authenticated:
        passengers_length = len(Passenger.objects.all())
        
        Flights_length = len(Flight.objects.all())
        Flights_true_length = len(Flight.objects.filter(available = 1))
        Flights_false_length = len(Flight.objects.filter(available = 0))

        Reservation_length = len(ReservationFlight.objects.all())
        Reservation_true_length = len(ReservationFlight.objects.filter(state =1))
        Reservation_false_length = len(ReservationFlight.objects.filter(state =0))

        context ={
            'passengers_length':passengers_length,
            'Flights_length':Flights_length,
            'Flights_true_length':Flights_true_length,
            'Flights_false_length':Flights_false_length,
            'Reservation_length':Reservation_length,
            'Reservation_true_length':Reservation_true_length,
            'Reservation_false_length':Reservation_false_length,
            'segment':'Reservation',
            'dashboard_type':'Reservation dashboard',
            }
        return render(request, 'home/index_reservation.html', context)
    else :
        return redirect ('login')

#User Controllerss
def user_list (request):
    users = User.objects.all()    
    print(User)
    context ={
        'users' : users,
        'segment':'users',
        'dashboard_type':'List Users',
        }
    return render(request, 'home/users/list.html', context)

def add_user (request):
    #ena lehna ................... 
    form  = CreateUserForm()
    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            
            user = form.save()  
            passenger = Passenger.objects.create(user=user, name= username , first_name = first_name, last_name= last_name, email= email)
            return redirect ('user_list')
        else :
            print (form.errors)
            messages.error(request,"Verif : ",form.errors)
    context ={
        'form':form ,
        'segment':'users',
        'dashboard_type':'Add User',
        }
    return render(request, 'home/users/form.html', context)

def show_user (request, pk):
    user = User.objects.get(id=pk)

    context ={
        'user':user,
        'segment':'users',
        'dashboard_type':'Show Users',
        }
    return render(request, 'home/users/show.html', context)

def delete_user (request,pk):
    user = User.objects.get(id=pk)
    
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    
    context ={
        'user':user,
        'segment':'users',
        'dashboard_type':'Delete Users',
        }
    return render(request, 'home/users/delete.html', context)

def update_user (request, pk):
    user = User.objects.get(id=pk)
    passenger = Passenger.objects.get (user =user)
    form = CreateUserForm(instance=user)

    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email'] 
              
            passenger.name = username
            passenger.first_name = first_name
            passenger.last_name = last_name
            passenger.email = email
            passenger.save()   
                    
            new_user = form.save()  

            return redirect('user_list')
        else :
            messages.error(request,"Verif User Passwords: ",form.errors)
        
    context ={
        'user':user,
        'form':form,
        'segment':'users',
        'dashboard_type':'Update Passengers',
        }
    return render(request, 'home/users/update.html', context)
    


#Passenger Controllerss
def passenger_list (request):
    passengers = Passenger.objects.all()    
    context ={
        'passengers' : passengers,
        'segment':'passengers',
        'dashboard_type':'List Passengers',
        }
    return render(request, 'home/passengers/list.html', context)

def add_passenger (request):
    form  = CreatePassengerForm()
    if request.method == 'POST' :
        #print('Printing POST', request.POST)
        form = CreatePassengerForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect ('passenger_list')
    context ={
        'form':form ,
        'segment':'passengers',
        'dashboard_type':'Add passengers',
        }
    return render(request, 'home/passengers/form.html', context)

def show_passenger (request, pk):
    passenger = Passenger.objects.get(id=pk)

    context ={
        'passenger':passenger,
        'segment':'passengers',
        'dashboard_type':'Show Passengers',
        }
    return render(request, 'home/passengers/show.html', context)

def delete_passenger (request,pk):
    passenger = Passenger.objects.get(id=pk)
    user = passenger.user
    if request.method == "POST":
        passenger.delete()
        user.delete()
        return redirect('passenger_list')
    
    context ={
        'passenger':passenger,
        'segment':'passengers',
        'dashboard_type':'Delete Passengers',
        }
    return render(request, 'home/passengers/delete.html', context)

def update_passenger (request,pk):
    passenger = Passenger.objects.get(id=pk)
    form = CreatePassengerForm(instance=passenger)
    
    if request.method == 'POST':
        form = CreatePassengerForm(request.POST, instance=passenger)
        if form.is_valid():            
            form.save()  
            return redirect('passenger_list')
        else :
            messages.error(request,"Verif Passenger Passwords: ",form.errors)
        
    context ={
        'form':form ,
        'segment':'passengers',
        'dashboard_type':'Update Passengers',
        }
    return render(request, 'home/passengers/update.html', context)
    
#flights Controllerss
def flights_list (request):
    flights = Flight.objects.all()
    
    context ={
        'flights':flights ,
        'segment':'flights',
        'dashboard_type':'List Flights',
        }
    return render(request, 'home/flights/list.html', context)

def add_flight (request):
    form  = CreateFlightForm()
    if request.method == 'POST' :
        form = CreateFlightForm(request.POST)
        if form.is_valid():
            instance = form.save()  
            instance.flight_duration = (instance.flight_end - instance.flight_start).total_seconds() //3600
            instance.save()

            return redirect ('flight_list')
        else:
            print("------------", form.errors)
            messages.error(request, form.errors)
    context ={
        'form':form ,
        'segment':'flights',
        'dashboard_type':'Add Flight',
        }
    return render(request, 'home/flights/form.html', context)

def show_flight (request, pk):
    flight = Flight.objects.get(id=pk)

    context ={
        'flight': flight,
        'segment':'flights',
        'dashboard_type':'Show flights',
        }
    return render(request, 'home/flights/show.html', context)

def delete_flight (request,pk):
    flight = Flight.objects.get(id=pk)
    
    if request.method == "POST":
        flight.delete()
        return redirect('flight_list')
    
    context ={
        'flight':flight,
        'segment':'flight',
        'dashboard_type':'Delete Flight',
        }
    return render(request, 'home/flights/delete.html', context)

def update_flight (request,pk):
    flight = Flight.objects.get(id=pk)
    form = CreateFlightForm(instance=flight)
    
    if request.method == 'POST':
        form = CreateFlightForm(request.POST, instance=flight)
        if form.is_valid():            
            instance = form.save()  
            instance.duration = (instance.flight_start - instance.flight_end).total_seconds() //3600
            instance.save()
            return redirect('flight_list')
                
    context ={
        'flight':flight,
        'form':form ,
        'segment':'flight',
        'dashboard_type':'Update Flight',
        }
    return render(request, 'home/flights/update.html', context)


#flights available Controllerss
def flights_available_list (request):
    flights = Flight.objects.filter(available=True)
    
    context ={
        'flights':flights ,
        'segment':'flights_available',
        'dashboard_type':'List Flights available',
        }
    return render(request, 'home/flights_available/list.html', context)

def flights_available_view (request, pk):
    flight = Flight.objects.get(id=pk)
    user = request.user
    passenger = Passenger.objects.get(user_id=user.id)
    
    form  = CreateFlightReservationForm()
    if request.method == 'POST' :
        form = CreateFlightReservationForm(request.POST)
        if form.is_valid():
            instance = form.save()  
            instance.passenger = passenger
            instance.flight = flight
            instance.state = False
            instance.save()
            
            ReservationFlightPredictions.objects.create(reservationFlight= instance, complete= "Pending Model Application")
            return redirect ('flights_available_list')
        else:
            print("------------", form.errors)
            messages.error(request, form.errors)
    context ={
        'form':form ,
        'flight':flight ,
        'segment':'flights_available',
        'dashboard_type':'Flights available To reservation',
        }
    return render(request, 'home/flights_available/show.html', context)

# reservation list 
def reservation_list (request):
    flight_resrvation = ReservationFlight.objects.all()
        
    context ={
        'flight_resrvation': flight_resrvation,
        'segment':'reservations',
        'dashboard_type':'List Reservations',
        }
    return render(request, 'home/reservation/list.html', context)

def show_reservation (request, pk):
    reservation = ReservationFlight.objects.get(id=pk)

    context ={
        'reservation': reservation,
        'segment':'reservations',
        'dashboard_type':'Show Reservation',
        }
    return render(request, 'home/reservation/show.html', context)

def delete_reservation (request,pk):
    reservation = ReservationFlight.objects.get(id=pk)
    
    reservationPredict = ReservationFlightPredictions.objects.get(reservationFlight_id=pk)

    if request.method == "POST":
        reservation.delete()
        reservationPredict.delete()
        return redirect('reservation_list')
    context ={
        'reservation':reservation,
        'segment':'reservations',
        'dashboard_type':'Delete Reservation',
        }
    return render(request, 'home/reservation/delete.html', context)

def make_reservation_true (request,pk):
    reservation = ReservationFlight.objects.get(id=pk)
    
    reservation.state = True
    reservation.save()
    return redirect('reservation_list')
    

#my reservation list 
def my_reservation_list (request):
    user = request.user
    passenger_ = Passenger.objects.get(user_id=user.id)
    print(passenger_)
    flight_resrvation = ReservationFlight.objects.filter(passenger_id =passenger_.id)
    print(flight_resrvation)
    context ={
        'flight_resrvation':flight_resrvation,
        'segment':'my_reservations',
        'dashboard_type':'List of my reservations',
        }
    return render(request, 'home/my_reservation/list.html', context)

def show_my_reservation (request, pk):
    reservation = ReservationFlight.objects.get(id=pk)

    context ={
        'reservation': reservation,
        'segment':'my_reservations',
        'dashboard_type':'Show My Reservation',
        }
    return render(request, 'home/my_reservation/show.html', context)


def delete_my_reservation (request,pk):
    reservation = ReservationFlight.objects.get(id=pk)
    reservationPredict = ReservationFlightPredictions.objects.get(reservationFlight_id=pk)
    
    if request.method == "POST":
        reservation.delete()
        reservationPredict.delete()
        
        return redirect('my_reservation_list')
    
    context ={
        'reservation':reservation,
        'segment':'my_reservations',
        'dashboard_type':'Delete My Reservation',
        }
    return render(request, 'home/my_reservation/delete.html', context)


#predict_reservation
def predict_reservation_list (request):
    reservation_predicted_list = ReservationFlightPredictions.objects.all()
    
    context ={
        'reservation_predicted_list':reservation_predicted_list,
        'segment':'predict_reservations',
        'dashboard_type':'List Reservations predicted',
        }
    return render(request, 'home/predict_reservation/list.html', context)

def predict_reservation_reset_all (request):
    reservation_predicted_list = ReservationFlightPredictions.objects.all()
    
    for i in reservation_predicted_list:
        i.complete = "Pending Model Application"
        i.save()
    
    reservation_predicted_list = ReservationFlightPredictions.objects.all()
    context ={
        'reservation_predicted_list':reservation_predicted_list,
        'segment':'predict_reservations',
        'dashboard_type':'List Reservations predicted',
        }
    return render(request, 'home/predict_reservation/list.html', context)

def predict_reservation_show (request,pk):
    reservation_predicted = ReservationFlightPredictions.objects.get(id=pk)
    
    
    context ={
        'reservation_predicted':reservation_predicted,
        'segment':'predict_reservations',
        'dashboard_type':'List Reservations predicted',
        }
    return render(request, 'home/predict_reservation/show.html', context)


def predict_reservation (request):
    reservation_predicted_list = ReservationFlightPredictions.objects.all()
    
    for i in reservation_predicted_list:
        #flight hour        
        # flight day
        date_obj = i.reservationFlight.flight.flight_start
        day = date_obj.day
        hour = date_obj.hour
        #Internet,Mobile
        if i.reservationFlight.sales_channel == "Mobile":
            Mobile =1
            Internet=0
        elif i.reservationFlight.sales_channel =='Internet' :
            Mobile =0
            Internet=1
        #RoundTRip,OneWayTrip,CircleTrip
        if i.reservationFlight.trip_type == 'RoundTrip' :
            RoundTRip= 1
            OneWayTrip=0
            CircleTrip=0
        elif i.reservationFlight.trip_type == 'CircleTrip' :
            RoundTRip= 0
            OneWayTrip=0
            CircleTrip=1
        elif i.reservationFlight.trip_type == 'OneWay' :
            RoundTRip= 0
            OneWayTrip=1
            CircleTrip=0
        L= [i.reservationFlight.number_of_chairs_to_reserve,
            i.reservationFlight.travel_duration, hour, day, i.reservationFlight.extra_baggage,
            i.reservationFlight.preffered_seat, i.reservationFlight.meal, i.reservationFlight.travel_duration,
            Internet, Mobile , RoundTRip, OneWayTrip, CircleTrip]
        result = model_predict(L)
        i.complete = result
        i.save()
    
    reservation_predicted_list = ReservationFlightPredictions.objects.all()
    
    context ={
        'reservation_predicted_list':reservation_predicted_list,
        'segment':'predict_reservations',
        'dashboard_type':'List Reservations predicted',
        }
    return render(request, 'home/predict_reservation/list.html', context)
#Export Csv 
def export_csv(request):
    reservation_predicted_list = ReservationFlightPredictions.objects.all()
    with open(r'C:\Users\Administrator\Desktop\file.csv','w' ,newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID RESERVATIONS','ID FLIGHT','ID PASSENGER','COMPLETION STATE (PREDICT)'])
        for row in reservation_predicted_list:
            writer.writerow([row.id, row.reservationFlight.flight.id, row.reservationFlight.passenger.id, row.complete])
    
    
    context ={
        'reservation_predicted_list':reservation_predicted_list,
        'segment':'predict_reservations',
        'dashboard_type':'List Reservations predicted',
        }
    return render(request, 'home/predict_reservation/list.html', context)
            
#profil update and show 
def user_profil (request):
    user = request.user
    form = CreateUserForm(instance=user)  
    if user.is_staff == True:
        will_update_pass = False
    else:
        will_update_pass = True
        passenger = Passenger.objects.get(user = user ) 
        
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            
            if will_update_pass == True :
                passenger.name = username
                passenger.first_name = first_name
                passenger.last_name = last_name
                passenger.email = email
                passenger.save()   
                       
            user = form.save()  

            return redirect('login')
        else :
            messages.error(request,"Verif User Passwords")
        
    context ={
        'user':user,
        'form':form,
        'segment':'profil',
        'dashboard_type':'My Profil',
        }
    return render(request, 'home/profile.html', context)
    