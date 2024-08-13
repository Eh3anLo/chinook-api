from rest_framework import serializers 
from .models import Album, Track, Artist

# class TrackSerializer(serializers.ModelSerializer):
#     album = serializers.SerializerMethodField()
#     duration = serializers.SerializerMethodField(source='milliseconds')
#     size = serializers.SerializerMethodField(source='bytes')

#     def get_album(self, obj):
#         return obj.album.title
    
#     def get_duration(self, obj):
#         minute = int((obj.milliseconds/1000)/60)
#         seconds = int((obj.milliseconds/1000)%60)
#         return f"{minute if minute >= 10 else '0'+str(minute)}:{seconds if seconds >= 10 else '0'+str(seconds)}"

#     def get_size(self, obj):
#         mgbyte = round(obj.bytes/2**20, 2)
#         return mgbyte
    
#     class Meta:
#         model = Track
#         fields = ['track_id', 'track_title', 'album', 'format', 'genre', 'artist', 'duration', 'size', 'unit_price']
#         extra_kwargs = {
#             'track_title' : {'source' : 'name'},
#             'format' : {'source' : 'media_type'},
#             'artist' : {'source' : 'composer'},

#         }
class TrackSerializer(serializers.Serializer):
    track_id = serializers.IntegerField()
    track_title = serializers.CharField(max_length=200, source='name')
    album = serializers.SerializerMethodField()
    format = serializers.CharField(source='media_type')
    genre = serializers.CharField()
    artist = serializers.CharField(max_length=220, source='composer')
    duration = serializers.SerializerMethodField(source='milliseconds')
    size = serializers.SerializerMethodField(source='bytes')
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def get_album(self, obj):
        return obj.album.title
    
    def get_duration(self, obj):
        minute = int((obj.milliseconds/1000)/60)
        seconds = int((obj.milliseconds/1000)%60)
        return f"{minute if minute >= 10 else '0'+str(minute)}:{seconds if seconds >= 10 else '0'+str(seconds)}"

    def get_size(self, obj):
        mgbyte = round(obj.bytes/2**20, 2)
        return mgbyte
    


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()

    def get_artist(self, obj):
        return obj.artist.name
    
    class Meta:
        model = Album
        fields = ('title', 'artist')



class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist_id' , 'artist_name']
        extra_kwargs = {
            'artist_name' : {'source' : 'name'}
        }