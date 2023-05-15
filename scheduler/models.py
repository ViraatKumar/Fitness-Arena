from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Schedule(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 100,default = "Rest Day")
    day = models.CharField(max_length = 20,primary_key = True)
class Exercise(models.Model):
    exercise = models.CharField(max_length=100)
    reps= models.IntegerField()
    sets = models.IntegerField()
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE,related_name="exercises")