from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from main.models import UserProfile, Post, Comment 
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
        
    post_data = forms.CharField(max_length=256, required=True)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = []
        
    comment_data = forms.CharField(max_length=256, required=True)