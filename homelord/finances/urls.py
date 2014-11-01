from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'finances.views.finances'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
