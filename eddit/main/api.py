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

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

'''
@:param id:Optional -> Returns a single post
@:param author:Optional -> Returns all posts by a single author
Returns all posts if no ID is passed in, otherwise filters by the appropriate identifier
JSON formatted
'''


def get_posts(request):
    if request.method == 'GET':
        if request.GET.get('id'):
            post_id = request.GET.get('id')
            posts = Post.objects.get(id=post_id)
        elif request.GET.get('author'):
            author = request.GET.get('author')
            posts = Post.objects.all().filter(author_id=author)
        else:
            posts = Post.objects.all()
        return HttpResponse(serializers.serialize('json', posts), content_type='application/json')
    return HttpResponse(status=405)  # Outlet responds to GET only


'''
@:param post:Required -> Post ID of post for which comments should be returned
Returns all comments for a corresponding post, JSON formatted
'''


def get_comments(request):
    if request.method == 'GET':
        if request.GET.get('post'):
            post = request.GET.get('post')
            comments = Comment.objects.all().filter(post_id=post)
            return HttpResponse(serializers.serialize('json', comments), content_type='application/json')
        return HttpResponse(status=400)  # Forgot post ID
    return HttpResponse(status=405)  # Outlet responds to GET only