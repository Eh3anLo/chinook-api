from rest_framework import serializers
from track.serializers import TrackSerializer
from track.models import Track
from .models import PlaylistTrack
class PlaylistSerializer(serializers.Serializer):
    playlist = serializers.StringRelatedField()
    track = serializers.SerializerMethodField()

    def get_track(self, obj):
        
        
        serializer = TrackSerializer(obj.track)
        return serializer.data