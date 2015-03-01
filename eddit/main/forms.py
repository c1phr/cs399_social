from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from main.models import User, UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = []
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']