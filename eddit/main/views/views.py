from django.core import serializers
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import PostForm, CommentForm
from django.template import RequestContext
from main.models.comment import Comment
from main.models.post import Post
from main.models.userprofile import UserProfile
from rest_framework import viewsets
from main.serializers import CommentSerializer, PostSerializer
from django.contrib.auth.decorators import user_passes_test


def home(request):
    return render(request, 'main/home.html', {})

def about(request):
    return render(request, 'main/about.html', {})

@user_passes_test(lambda u: u.is_superuser)
def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(post)
    return render_to_response('main/add_post.html', 
                              { 'form': form },
                              context_instance=RequestContext(request))
                              
def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render_to_response('main/blog_post.html',
                              {
                                  'post': post,
                                  'form': form,
                              },
                              context_instance=RequestContext(request))