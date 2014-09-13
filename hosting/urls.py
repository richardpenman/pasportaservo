from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns('hosting.views',
    url(r'^$', 'home', name='home'),
    url(_(r'^register/$'), 'register', name='register'),
    url(_(r'^profile/create/$'), 'profile_create', name='profile_create'),
    url(_(r'^profile/detail/$'), 'profile_detail', name='profile_detail'),
    url(_(r'^place/create/$'), 'place_create', name='place_create'),
    url(_(r'^place/(?P<pk>\d+)/update/$'), 'place_update', name='place_update'),
    url(_(r'^place/(?P<pk>\d+)/$'), 'place_detail', name='place_detail'),
    url(_(r'^search/$'), 'search', name='search'),
)