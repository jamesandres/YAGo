from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import (RedirectView, TemplateView)

import go.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt'),
        {'mimetype': 'text/plain'}),

    url(r'^$', go.views.ListGamesView.as_view(), name='list-games'),

    url(r'^g/(?P<pk>\d+)$', go.views.GameView.as_view(), name='game'),

    url(r'^g/(?P<pk>\d+)/play$',
        go.views.APIPlayView.as_view(), name='api-play'),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'admin/login.html'}),
    url(r'^accounts/$', RedirectView.as_view(url='/')),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
