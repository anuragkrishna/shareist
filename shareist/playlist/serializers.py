from rest_framework import serializers
from playlist.models import Track, Playlist
from django.contrib.auth.models import User

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ('url', 'title', 'link', 'artist', 'owner', 'added_date')

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ('url', 'owner','title', 'created_date', 'tracks')       

class UserSerializer(serializers.HyperlinkedModelSerializer):
    playlists = serializers.HyperlinkedRelatedField(many=True,view_name='playlist-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ('url', 'username', 'owner', 'playlists') 