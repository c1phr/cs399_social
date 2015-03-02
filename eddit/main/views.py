from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import UserForm, UserProfileForm
from django.template import RequestContext
from main.models.comment import Comment
from main.models.post import Post


def home(request):
    return render(request, 'main/home.html', {})


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.post, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            phonenumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                           error_message=(
                                               "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return HttpResponseRedirect('main/home.html')
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render_to_response('main/register.html',
                              dict(userform=uf,
                                   userprofileform=upf),
                              context_instance=RequestContext(request))


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