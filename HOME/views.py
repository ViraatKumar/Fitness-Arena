from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from scheduler import models as scheduler_models
from . import forms
from . import models 
# import requests
from scheduler import views as scheduler
import json
from pprint import pprint
# Create your views here.
days = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]
def fill_schedueler(request):
    
    user = request.user

    for day in days:
        obj = scheduler_models.Schedule(user=user,day=day,name="Rest Day")
        obj.save()
        
def form_id_select(arg):
    if arg=="login":
        return "login-form-view"
    else:
        return "login-form-view block"
def reg_id_select(arg):
    if arg=="register":
        return "register-form-view"
    else:
        return "register-form-view block"
def homepage(request):
    return render(request,"homepage.html",{})
def loginreg(request):
    print(request.POST)
    if(request.method  =="POST"):
        if 'loginform' in request.POST:
            username= request.POST.get("username")
            password = request.POST.get("password")
            print()
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                # redirects to scheduler app
                return redirect("userpage")
                
            else:
                error_message = "Username or Password is incorrect"
                context = {
                    "message":error_message,
                }
                return render(request,"login_reg.html",context)
        else:
            username = request.POST.get("reg_username")
            password = request.POST.get("create_password")
            if(User.objects.filter(username=username).exists()):
                error_message = "User already Exists.\nLog in here"
                context = {
                    "message":error_message,
                }
                return render(request,"login_reg.html",context)

            else:
                # new user is being created
                user = User.objects.create_user(username=username,password=password)
                context = {
                    "user":user.username,
                }
                login(request,user)
                fill_schedueler(request)
                return redirect("userpage")
                
    context={
    }
    return render(request,"login_reg.html",context)