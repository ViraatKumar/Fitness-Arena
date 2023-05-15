from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from . import forms
from . import models
# Create your views here.

# def testing(user,day,reps,sets):
#     e1 = models.Exercise.objects.create(exercise="benchpress",reps=0,sets=0)
#     e2 = models.Exercise.objects.create(exercise="leggpress",reps=0,sets=0)
#     models.Schedule.objects.create(user=user,day=day,exercise=[e1,e2],name="chestday")
#     obj = models.Schedule.objects.filter(uesr=user,day=day)
#     for i in obj:
#         print(i)
days = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]
def logout_user(request):
    logout(request)
    return redirect("homepage")
def userpage(request):
    if(request.method=="POST"):
        print("--------SEE THIS--------")
        print(request.POST)
        day = request.POST.get('day')
        name = request.POST.get('name')
        count = request.POST.get('count')
        models.Schedule.objects.filter(user=request.user,day = day.lower()).update(name=name)
        obj = models.Schedule.objects.get(user=request.user,day=day)
        models.Exercise.objects.filter(schedule=obj).delete()
        try:
            for i in range(1,int(count)+1):
                ex = "exercise"+str(i)
                reps = "reps"+str(i)
                sets="sets"+str(i)
                exercise_name = request.POST.get(ex)
                num_of_reps=request.POST.get(reps)
                num_of_sets = request.POST.get(sets)
                models.Exercise.objects.create(exercise=exercise_name,reps=num_of_reps,sets=num_of_sets,schedule=obj)
        except ValueError:  
            print("no exercises chosen")
        
        obj = models.Schedule.objects.filter(user = request.user)
        print(obj)
        context = {
            "user":request.user,
            "days":days,
            "obj":obj,
        }
        return render(request,"userPage.html",context)
         
    obj = models.Schedule.objects.filter(user = request.user)
    print(obj)
    context = {
        "user":request.user,
        "days":days,
        "obj":obj,
    }
    return render(request,"userPage.html",context)
def newworkout(request):
    if request.method == "POST":
        print(request.POST)
        day = request.POST.get('day-name')
        workout = request.POST.get('workout-name')
        context = {
            "day":day,
            "workout":workout
        }
        return render(request,"assign_workout.html",context)
    context = {}
    return render(request,"assign_workout.html",context)
def viewworkout(request):
    print(request.POST )
    if request.method == "POST":
        day = request.POST.get('day-name')
        workout = request.POST.get("workout-name")
        obj = models.Schedule.objects.get(day=day.lower())
        exercises = obj.exercises.all()
        context = {
            "day":day,
            "workout":workout,
            "exercises":exercises,
        }
        return render(request,"view_workouts.html",context)
    context = {}
    return render(request,"assign_workout.html",context)
def  calculator(request):
    if request.method == 'POST':
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        activity_level = request.POST.get('activity_level')
        
        # Convert height to centimeters
        height_cm = float(height) * 2.54
        
        # Calculate the user's BMR (Basal Metabolic Rate)
        if gender == 'male':
            bmr = 88.362 + (13.397 * float(weight)) + (4.799 * height_cm) - (5.677 * float(age))
        elif gender == 'female':
            bmr = 447.593 + (9.247 * float(weight)) + (3.098 * height_cm) - (4.330 * float(age))
        
        # Calculate the user's TDEE (Total Daily Energy Expenditure) based on their activity level
        if activity_level == 'sedentary':
            tdee = bmr * 1.2
        elif activity_level == 'lightly_active':
            tdee = bmr * 1.375
        elif activity_level == 'moderately_active':
            tdee = bmr * 1.55
        elif activity_level == 'very_active':
            tdee = bmr * 1.725
        elif activity_level == 'extra_active':
            tdee = bmr * 1.9
        
        # Round the result to the nearest whole number
        tdee = round(tdee)
        
        # Pass the calculated TDEE to the template as a context variable
        context = {'tdee': tdee}
        return render(request, 'calculator.html', context)
    
    return render(request, 'calculator.html')
