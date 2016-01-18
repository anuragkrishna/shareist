from playlist.models import Playlist, Track
from playlist.serializers import PlaylistSerializer, TrackSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics
from shareist.permissions import IsPlaylistOwner
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'playlists': reverse('playlist-list', request=request, format=format),
        'tracks': reverse('track-list', request=request, format=format)
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#/playlist
class Playlist_List(APIView):

	permission_classes=(permissions.IsAuthenticated, IsPlaylistOwner)

	def get(self, request, format=None):
		playlists = Playlist.objects.all().filter(owner=request.user)
		serializer = PlaylistSerializer(playlists, many=True, context={'request': request})
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = PlaylistSerializer(data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)	

#/playlist/<pk>
class Playlist_Detail(APIView):

    permission_classes = (permissions.IsAuthenticated,IsPlaylistOwner)

    def get_object(self, pk, request):
    	try:
    		return Playlist.objects.get(pk=pk, owner=request.user)
    	except Playlist.DoesNotExist:
    		raise Http404

    def get(self, request, pk, format=None):
    	playlist = self.get_object(pk, request)
    	serializer = PlaylistSerializer(playlist, context={'request': request})
    	return Response(serializer.data)

    def put(self, request, pk, format=None):
    	playlist = self.get_object(pk)
    	serializer = PlaylistSerializer(playlist, data=request.data, context={'request': request})
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
    	playlist = self.get_object(pk)
    	playlist.delete()
    	return Response(status=status.HTTP_204_NO_CONTENT)        

#/track
class Track_List(APIView):

	permission_classes=(permissions.IsAuthenticated, IsPlaylistOwner)

	def get(self, request, format=None):
		tracks = Track.objects.all().filter(owner=request.user)
		serializer = TrackSerializer(tracks, many=True, context={'request': request})
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = TrackSerializer(data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#track/<pk>
class Track_Detail(APIView):

	permission_classes=(permissions.IsAuthenticated, IsPlaylistOwner)
	def get_object(self, pk, request):
		try:
			return Track.objects.get(pk=pk, owner=request.user)
		except Track.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		track = self.get_object(pk, request)
		serializer = TrackSerializer(track, context={'request': request})
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		track = self.get_object(pk)
		serializer = TrackSerializer(track, data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		track = self.get_object(pk)
		track.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)            
