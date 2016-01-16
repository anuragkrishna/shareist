from rest_framework import serializers
from playlist.models import Track, Playlist

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'title', 'url', 'artist', 'owner', 'added_date', 'playlist', 'shared_with')

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('id', 'author','title', 'created_date', 'shared_with')        