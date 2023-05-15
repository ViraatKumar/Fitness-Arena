from django.forms import ModelForm
from django import forms
from . import models

class Schedule(forms.Form):
    name = forms.CharField(label = "Exercise",max_length = 100, widget=forms.TextInput(attrs={
        "placeholder":"Eg: Bench Press",
    }))
    reps = forms.IntegerField()
    sets = forms.IntegerField()
activity_levels = {
    ("sedentary","Sedentary"),
    ("lightly_active","Lightly Active"),
    ("moderate","Moderate Active"),
    ("very_active","Very Active"),
    ("extra_active","Extra Active"),
}

class Calculator(forms.Form):
    height= forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder":"cm",
        }
    ))
    weight=forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder":"kg",
        }
    ))
    activity_level = forms.ChoiceField(choices=activity_levels)


    