from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.utils import timezone

class Track(models.Model):
	title = models.CharField(max_length=100)
	link =  models.URLField(max_length=1000)
	artist = models.CharField(max_length=100, default='unknown')
	added_date = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey('auth.User', related_name='tracks')
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)

class Playlist(models.Model):
	owner = models.ForeignKey('auth.User', related_name='playlists')
	title = models.CharField(max_length=50)
	created_date = models.DateTimeField(default=timezone.now)
	tracks = models.ManyToManyField(Track, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)

