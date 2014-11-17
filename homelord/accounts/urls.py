from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView


urlpatterns = patterns('',
                       url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^register', 'accounts.views.register', name='register'),
                       url(r'^$', TemplateView.as_view(template_name='main.html'), name='main'),
                       url(r'^admin/', include(admin.site.urls)),
)
