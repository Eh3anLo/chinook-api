from django.db import models

# Create your models here.

class Playlist(models.Model):
    playlist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'playlist'


class PlaylistTrack(models.Model):
    playlist_track_id = models.AutoField(primary_key=True,auto_created=True)
    playlist = models.ForeignKey(Playlist, models.CASCADE)  # The composite primary key (playlist_id, track_id) found, that is not supported. The first column is selected.
    track = models.ForeignKey('track.Track', models.DO_NOTHING, related_name='track')

    class Meta:
        db_table = 'playlist_track'
