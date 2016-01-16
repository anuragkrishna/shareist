from django.db import models
from django.utils import timezone

class Playlist(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=50)
	created_date = models.DateTimeField(default=timezone.now)
	shared_with = models.ManyToManyField('auth.User', related_name='shared_Playlist', blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)


class Track(models.Model):
	title = models.CharField(max_length=100)
	url =  models.URLField(max_length=1000)
	artist = models.CharField(max_length=100, default='unknown')
	added_date = models.DateTimeField(default=timezone.now)
	playlist = models.ManyToManyField(Playlist, blank=True)
	owner = models.ForeignKey('auth.User')
	shared_with = models.ManyToManyField('auth.User', related_name='shared_Track', blank=True)
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)
    


