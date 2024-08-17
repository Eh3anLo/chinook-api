from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('artists', views.ArtistViewSet)

urlpatterns = [
    path('tracks/', views.TrackListView.as_view(), name="track-list"),
    path('albums/', views.AlbumListView.as_view(), name="album-list"),
    path('', include(router.urls))
]