from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'searches.views.searches', name='search'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
