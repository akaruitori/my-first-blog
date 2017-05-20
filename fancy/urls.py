from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'fancy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'', include('blog.urls')),
]
