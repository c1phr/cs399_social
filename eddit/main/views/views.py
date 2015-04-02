from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import UserProfileForm, PostForm, CommentForm
from django.template import RequestContext
from main.models.comment import Comment
from main.models.post import Post
from main.models.userprofile import UserProfile
from rest_framework import viewsets
from main.serializers import CommentSerializer, PostSerializer


def home(request):
    return render(request, 'main/home.html', {})

def about(request):
    return render(request, 'main/about.html', {})


def register(request):
    if request.method == 'POST':
        upf = UserProfileForm(request.POST)
        if upf.is_valid():
            u = UserProfile()
            u.phone_number = upf.cleaned_data["phone_number"]
            u.first_name = upf.cleaned_data["first_name"]
            u.last_name = upf.cleaned_data["last_name"]
            u.user_name = upf.cleaned_data["user_name"]
            u.save()
            return HttpResponseRedirect("/")
    elif request.method == 'GET':
        upf = UserProfileForm()
    else:
        return HttpResponseRedirect("/404/")
    return render(request, 'register.html', {"upf": upf})