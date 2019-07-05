from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length = 50)
    album = models.CharField(max_length = 50)
    song = models.CharField(max_length = 50)
