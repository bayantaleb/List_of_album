from rest_framework import serializers
from music.models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('artist', 'albums', 'song') 
