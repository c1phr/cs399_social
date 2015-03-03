from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from main.models import UserProfile, Post, Comment
   

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = []

    email = forms.EmailField(label="Your email", required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    first_name = forms.CharField(max_length=128, required=True)
    last_name = forms.CharField(max_length=128, required=True)
    user_name = forms.CharField(max_length=128, required=True)
    
    
class PostForm(forms.ModelForm):
    post_data = forms.CharField(max_length=256, required=True)
    
class CommentForm(forms.ModelForm):
    comment_data = forms.CharField(max_length=256, required=True)