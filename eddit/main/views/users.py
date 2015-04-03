import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required
def users(request):
	user_name = request.GET.get('username', None)
	return render(request, "main/user.html", {'all_users': User.objects.all(), 'user' : User.objects.filter(username=user_name)})

@login_required
def profile(request):
	user_name = request.GET.get(pk=int(id))
	return render(request, "main/profile.html", { 'user' : User.objects.get(pk=int(id))})

@login_required
def ryan(request):
	return render(request, "main/dooley.html")

@login_required
def keevan(request):
	return render(request, "main/keevan.html")

@login_required
def justin(request):
	return render(request, "main/justin.html")