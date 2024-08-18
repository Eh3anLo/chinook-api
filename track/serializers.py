from rest_framework import serializers 
from .models import Album, Track, Artist,Genre,MediaType

class TrackSerializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(read_only=True, slug_field='title')
    duration = serializers.SerializerMethodField(source='milliseconds')
    size = serializers.SerializerMethodField(source='bytes')
    genre = serializers.StringRelatedField()
    file_format = serializers.StringRelatedField(source='media_type')
    
    def get_duration(self, obj):
        minute = int((obj.milliseconds/1000)/60)
        seconds = int((obj.milliseconds/1000)%60)
        return f"{minute if minute >= 10 else '0'+str(minute)}:{seconds if seconds >= 10 else '0'+str(seconds)}"

    def get_size(self, obj):
        mgbyte = round(obj.bytes/2**20, 2)
        return mgbyte
    
    class Meta:
        model = Track
        fields = ['track_id', 'track_title', 'album', 'genre','file_format', 'artist', 'duration', 'size', 'unit_price']
        extra_kwargs = {
            'track_title' : {'source' : 'name'},
            'artist' : {'source' : 'composer'},
        }



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields= '__all__'



class MediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaType
        fields= '__all__'


class TrackCreateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Track
        fields = ['track_id', 'name', 'album', 'genre','media_type', 'composer', 'milliseconds', 'bytes', 'unit_price']


class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('album_id','title', 'artist_id','artist_name')
        extra_kwargs = {
            'artist_id': {'source' : 'artist'}
        }



class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist_id' , 'artist_name']
        extra_kwargs = {
            'artist_name' : {'source' : 'name'}
        }