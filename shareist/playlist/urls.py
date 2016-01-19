"""shareist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

playlist_list = views.PlaylistViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
playlist_detail = views.PlaylistViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

track_list = views.TrackViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
track_detail = views.TrackViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^api/$', views.api_root),

    url(r'^api/playlist/$',playlist_list, name='playlist-list'),
    url(r'^api/playlist/(?P<pk>[0-9]+)/$', playlist_detail,name='playlist-detail'),

    url(r'^api/track/$',track_list, name='track-list'),
    url(r'^api/track/(?P<pk>[0-9]+)/$', track_detail,name='track-detail'),

    url(r'^api/users/$', user_list, name='user-list'),
	url(r'^api/users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
