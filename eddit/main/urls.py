from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', api.PostViewSet)
router.register(r'comments', api.CommentViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^$', 'main.views.views.home', name='home'),
    url(r'^about/', 'main.views.views.about', name='about'),
    url(r'^register/', 'main.views.register.new_user', name='newuser'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$', 'django.contrib.auth.views.login', {
    'template_name': 'main/login.html'
    }),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)