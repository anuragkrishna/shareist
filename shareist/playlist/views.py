from playlist.models import Playlist, Track
from playlist.serializers import PlaylistSerializer, TrackSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets



#/api/
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'playlists': reverse('playlist-list', request=request, format=format),
        'tracks': reverse('track-list', request=request, format=format)
    })


#api/user
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#/api/playlist
class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer
    permission_classes=[permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.request.user.playlists.all()

    def perform_create(self, serializer):
        serializer.data.owner = self.request.user
        super(PlaylistViewSet, self).perform_create(serializer)

#/api/track
class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    permission_classes=[permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.request.user.tracks.all()
        
    def perform_create(self, serializer):
        serializer.data.owner = self.request.user
        super(TrackViewSet, self).perform_create(serializer)        
              
