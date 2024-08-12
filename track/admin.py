from django.contrib import admin
from . import models
# Register your models here.

class MediaTypeAdmin(admin.ModelAdmin):
    list_display = ['pk','name']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['pk','name']


class TrackAdmin(admin.ModelAdmin):
    list_display = ['track_id','name','media_type','genre','track_durations','unit_price']

    @admin.display(description="duration")
    def track_durations(self, obj):
        minute = int((obj.milliseconds/1000)/60)
        seconds = int((obj.milliseconds/1000)%60)
        return f"{minute if minute >= 10 else '0'+str(minute)}:{seconds if seconds >= 10 else '0'+str(seconds)}"



class ArtistAdmin(admin.ModelAdmin):
    list_display = ['artist_id', 'name']



class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_id', 'title', 'artist']

admin.site.register(models.Album, AlbumAdmin)
admin.site.register(models.Artist, ArtistAdmin)
admin.site.register(models.Track, TrackAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.MediaType, MediaTypeAdmin)