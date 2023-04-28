from django.shortcuts import render, redirect
from django.contrib import messages
from .form import *
from .models import *

from django.contrib.auth import login, logout, authenticate
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def register (request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['password1']

            user = form.save()  
            passenger = Passenger.objects.create(user=user, name= username , email= email)
   
            user = authenticate(username=username, password=raw_password)

            messages.success(request, 'Account was created for ' + username)
            return redirect('dashboard')
       
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

#@csrf_exempt
def login_page (request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' :
        form = LoginForm(request.POST)
        if form.is_valid():
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate( request , username= username ,password= password)
           if user is not None :
               login(request , user)
               return redirect('dashboard')
           else :
                messages.error(request, "Username or password are false")
    context={'form':form}
    return render(request , 'accounts/login.html', context)


def logoutUser (request):
    logout(request)
    return redirect ('login')