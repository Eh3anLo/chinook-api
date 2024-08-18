from django.db import models

# Create your models here.

class MediaType(models.Model):
    media_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, blank=True, null=True)


    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'media_type'



class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genre'



class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=160)
    artist = models.ForeignKey('Artist', models.DO_NOTHING)

    def __str__(self):
        return f'{self.title} by {self.artist.name}'

    class Meta:
        db_table = 'album'



class Track(models.Model):
    track_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, models.DO_NOTHING, blank=True, null=True)
    media_type = models.ForeignKey(MediaType, models.DO_NOTHING)
    genre = models.ForeignKey(Genre, models.CASCADE)
    composer = models.CharField(max_length=220, blank=True, null=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
       
        return f'{self.name} by {self.composer}'

    class Meta:
        db_table = 'track'



class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist'


