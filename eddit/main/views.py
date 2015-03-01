from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from main.forms import UserForm, UserProfileForm
from django.template import RequestContext

def home(request):
    return render(request, 'main/home.html', {})

def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf  = UserProfileForm(request.post, prefix='userprofile')
        if uf.is_valid() * upf .is_valid():
            phonenumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return HttpResponseRedirect('main/home.html')
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render_to_response('main/register.html',
                                             dict(userform = uf,
                                                userprofileform = upf),
                                                context_instance = RequestContext(request))