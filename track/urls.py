from django.urls import path
from . import views
urlpatterns = [
    path('tracks/', views.TrackListView.as_view(), name="track-list"),
    path('albums/', views.AlbumListView.as_view(), name="album-list"),
    path('artists/', views.ArtistListView.as_view(), name='artist-list')
]