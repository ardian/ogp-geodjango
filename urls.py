from django.conf.urls.defaults import patterns, include, url
from django.contrib.gis import admin

#admin.autodiscover()

#urlpatterns = patterns('',
#	(r'^admin/', include(admin.site.urls)),
#)
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geodjango.views.home', name='home'),
    # url(r'^geodjango/', include('geodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#Uncomment the next line to enable the admin:
url(r'^admin/', include(admin.site.urls)),
)
#from django.contrib.gis import admin
