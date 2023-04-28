from django.forms import ModelForm
from django import forms
from authentication.models import Passenger
from .models import Flight
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    
    email = forms.EmailField(
        widget= forms.EmailInput(
            attrs={
                "placeholder": "Adress mail",
                "class": "form-control"
                
            }
        ))
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "placeholder": "Password ",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "placeholder": "Check Password",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = User
        fields = ['username', 'first_name' ,'last_name' ,'email', 'password1', 'password2']
  

class CreatePassengerForm (ModelForm):

    name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                "readonly": True
            }
        ))
    
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control",
                "readonly": True

            }
        ))
    
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control",
                "readonly": True
            }
        ))
    
    phone = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Phone",
                "class": "form-control"
            }
        ))
    
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Mail Adress",
                "class": "form-control",
                "readonly": True
            }
        ))
    
    adress = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Adress",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = Passenger
        fields = ['name', 'first_name' , 'last_name' , 'phone', 'email', 'adress']
        

class CreateFlightForm (ModelForm):
    flight_UID = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Flight UID",
                "class": "form-control",
            }
        ))
    flight_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "Flight Name",
                "class": "form-control",
            }
        ))
           
    flight_start = forms.DateTimeField(
        widget= forms.DateTimeInput(
            attrs={
                "placeholder": "Flight start day",
                "class": "form-control" ,
                "type" : "datetime-local"
            }
        )#,input_formats=['%Y-%m-%d %H:%M:%S']
        )
   
    flight_end = forms.DateTimeField(
        widget= forms.DateTimeInput(
            attrs={
                "placeholder": "Flight end day",
                "class" : "form-control" ,
                "type" : "datetime-local"
                }
        )#,input_formats=['%Y-%m-%d %H:%M:%S']
        )

    From = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "From",
                "class": "form-control",
            }
        ))
    To = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "placeholder": "To",
                "class": "form-control",
            }
        ))
    CHOICES = [(True, 'Yes'), (False, 'No')]
    available = forms.ChoiceField(
        choices=CHOICES,
        widget= forms.RadioSelect (
            
        ))
    class Meta:
        model = Flight
        fields = ['flight_name', 'flight_UID' , 'flight_start', 'flight_end','From','To' , 'available' ]
        
    def clean(self):
        cleaned_data = super().clean()
        flight_start = cleaned_data.get("flight_start")
        flight_end = cleaned_data.get("flight_end")
        if flight_start and flight_end:
            if flight_start >= flight_end:
                raise forms.ValidationError("Flight start must be less than flight end")