from rest_framework import serializers
from track.serializers import TrackSerializer
from track.models import Track
from .models import Playlist, PlaylistTrack

class PlaylistSerializer(serializers.ModelSerializer):
    total_tracks = serializers.SerializerMethodField()
    tracks = serializers.SerializerMethodField()

    def get_tracks(self, obj):
        tracks_in_list = PlaylistTrack.objects.filter(playlist=obj.playlist_id).values_list('track_id', flat=True)
        tracks = Track.objects.filter(track_id__in=tracks_in_list).select_related('album','genre','media_type')
        serializer = TrackSerializer(tracks, many=True)
        return serializer.data
        

    def get_total_tracks(self, obj):
        tracks_count = PlaylistTrack.objects.filter(playlist=obj.playlist_id).count()
        return tracks_count

    class Meta:
        model = Playlist
        fields = ('playlist_id' , 'playlist_title', 'total_tracks','tracks')
        extra_kwargs = {
            'playlist_title' : {'source' : 'name'}
        }



class PlaylistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'