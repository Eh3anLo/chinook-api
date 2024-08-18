from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('artists', views.ArtistViewSet)
router.register('albums', views.AlbumViewSet)
router.register('genres', views.GenreViewSet)
router.register('media-types', views.MediaTypeViewSet)

urlpatterns = [
    path('tracks/', views.TrackListView.as_view(), name="track-list"),
    path('tracks/<int:pk>/', views.TrackRetreiveUpdateDestroyApiView.as_view()),
    path('tracks/search/', views.TrackSearchApiView.as_view(), name='track-search'),

    path('', include(router.urls)),
]