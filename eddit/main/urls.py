from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^about/', 'main.views.about', name='about'),
    url(r'^register/$', 'main.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$', 'django.contrib.auth.views.login', {
    'template_name': 'main/login.html'
    }),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)