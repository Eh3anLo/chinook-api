from django.db import models

# Create your models here.

class Playlist(models.Model):
    playlist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'playlist'


class PlaylistTrack(models.Model):
    playlist = models.OneToOneField(Playlist, models.DO_NOTHING, primary_key=True)  # The composite primary key (playlist_id, track_id) found, that is not supported. The first column is selected.
    track = models.ForeignKey('track.Track', models.DO_NOTHING)

    class Meta:
        db_table = 'playlist_track'
        unique_together = (('playlist', 'track'),)
