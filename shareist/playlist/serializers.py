from rest_framework import serializers
from playlist.models import Track, Playlist
from django.contrib.auth.models import User

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'title', 'url', 'artist', 'owner', 'added_date', 'playlist', 'shared_with')

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('id', 'owner','title', 'created_date', 'shared_with')       

class UserSerializer(serializers.ModelSerializer):
    playlists = serializers.PrimaryKeyRelatedField(many=True, queryset=Playlist.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ('id', 'username', 'playlists', 'owner') 