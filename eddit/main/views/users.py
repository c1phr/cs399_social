import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required
def users(request):
	user_name = request.GET.get('username', None)
	return render(request, "main/user.html", {'all_users': User.objects.all(), 'user' : User.objects.filter(username=user_name)})