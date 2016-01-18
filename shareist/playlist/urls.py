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

urlpatterns = [
    url(r'^api/$', views.api_root),
    url(r'^api/playlist/$',views.Playlist_List.as_view(), name='playlist-list'),
    url(r'^api/playlist/(?P<pk>[0-9]+)/$', views.Playlist_Detail.as_view(),name='playlist-detail'),

    url(r'^api/track/$',views.Track_List.as_view(), name='track-list'),
    url(r'^api/track/(?P<pk>[0-9]+)/$', views.Track_Detail.as_view(),name='track-detail'),

    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
	url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
