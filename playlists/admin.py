from django.contrib import admin
from . import models
# Register your models here.
class PlayListAdmin(admin.ModelAdmin):
    list_display = ['playlist_id', 'name']


class PlayListTrackAdmin(admin.ModelAdmin):
    list_display = ['playlist', 'track']

admin.site.register(models.Playlist, PlayListAdmin)
admin.site.register(models.PlaylistTrack, PlayListTrackAdmin)