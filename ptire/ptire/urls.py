from django.conf.urls import patterns, include, url
from django.views.static import *
from django.conf import settings
from frontpage.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'frontpage.views.home', name='home'),
    url(r'^system/carstatus$', 'frontpage.views.carstatus', name='carstatus'),
    url(r'^pro/(\w+)/$','frontpage.views.pro',name='pro'),
    #url(r'^$', 'frontpage.views.home', name='home'),
    # url(r'^ptire/', include('ptire.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Internatinale
    (r'^i18n/', include('django.conf.urls.i18n')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	# MEDIA files
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),


)
