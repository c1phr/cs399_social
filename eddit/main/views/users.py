import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from main.models.post import Post


@login_required
def users(request):
	user_name = request.GET.get('username', None)
	return render(request, "main/user.html", {'all_users': User.objects.all(), 'current_user' : User.objects.filter(username=user_name)})

@login_required
def profile(request):
	userid = request.GET.get("id", "")
	user = User.objects.filter(id = userid).first()
	return render(request, "main/profile.html", { 'user' : user, 'posts': Post.objects.filter(author=user)})