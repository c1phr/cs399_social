from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import PostForm, CommentForm
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