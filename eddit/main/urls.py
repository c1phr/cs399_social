from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns('',
    
    url(r'^$', 'main.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$', 'django.contrib.auth.views.login', {
    'template_name': 'main/login.html'
    }),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)