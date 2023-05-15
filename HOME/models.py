from django.db import models

class user(models.Model):
    
    username = models.CharField(max_length = 100,primary_key=True)
    password = models.CharField(max_length = 100)