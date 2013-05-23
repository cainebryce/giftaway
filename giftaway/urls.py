from django.conf.urls import patterns, include, url
from giftplanner.api import GiftResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

gift_resource = GiftResource()

urlpatterns = patterns('',
    url(r'^$', 'giftplanner.views.home', name='home'),
    # url(r'^giftplanner/', include('giftplanner.urls')),
    # Examples:
    # url(r'^$', 'giftaway.views.home', name='home'),
    # url(r'^giftaway/', include('giftaway.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(gift_resource.urls)),
)
