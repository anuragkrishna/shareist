from playlist.models import Playlist, Track
from playlist.serializers import PlaylistSerializer, TrackSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#/playlist
class Playlist_List(APIView):

    def get(self, request, format=None):
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#/playlist/<pk>
class Playlist_Detail(APIView):

	def get_object(self, pk):
		try:
			return Playlist.objects.get(pk=pk)
		except Playlist.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		playlist = self.get_object(pk)
		serializer = PlaylistSerializer(playlist)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		playlist = self.get_object(pk)
		serializer = PlaylistSerializer(playlist, data=request.data)
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

    def get(self, request, format=None):
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#track/<pk>
class Track_Detail(APIView):

	def get_object(self, pk):
		try:
			return Track.objects.get(pk=pk)
		except Track.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		track = self.get_object(pk)
		serializer = TrackSerializer(track)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		track = self.get_object(pk)
		serializer = TrackSerializer(track, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		track = self.get_object(pk)
		track.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)            
