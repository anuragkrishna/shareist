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
    queryset = Playlist.objects.all()

    def get_queryset(self):
        return self.request.user.playlists.all()

    def perform_create(self, serializer):
        serializer.data.owner = self.request.user
        super(PlaylistViewSet, self).perform_create(serializer)

#/api/playlist
class PlaylistTrackViewSet(viewsets.ViewSet):
    queryset = Playlist.objects.all()

    def get_queryset(self, pk):
        return self.request.user.playlists.all().filter(pk=pk)
    
    def list(self, request, playlist_pk=None):
        playlist = Playlist(self.get_queryset(playlist_pk))
        playlist_tracks = playlist.tracks
        serializer = TrackSerializer(playlist_tracks , many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None, playlist_pk=None):
        playlist = Playlist(self.get_queryset(playlist_pk))
        playlist_track = playlist.tracks.all().get(pk=pk)
        serializer = TrackSerializer(playlist_track, context={'request': request})
        return Response(serializer.data)       

#/api/track
class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    permission_classes=[permissions.IsAuthenticated, ]
    queryset = Track.objects.all()

    def get_queryset(self):
        return self.request.user.tracks.all()
        
    def perform_create(self, serializer):
        serializer.data.owner = self.request.user
        super(TrackViewSet, self).perform_create(serializer)        
              
