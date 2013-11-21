from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import go.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$', go.views.ListGamesView.as_view(), name='list-games'),

    url(r'^(?P<pk>\d+)$', go.views.GameView.as_view(), name='game'),

    url(r'^(?P<kifu_id>\d+)/play$',
        go.views.APIPlayView.as_view(), name='api-play'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
