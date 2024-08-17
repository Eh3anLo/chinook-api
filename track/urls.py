from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('artists', views.ArtistViewSet)
router.register('albums', views.AlbumViewSet)

urlpatterns = [
    path('tracks/', views.TrackListView.as_view(), name="track-list"),
    path('tracks/<int:pk>/', views.TrackRetreiveUpdateDestroyApiView.as_view()),
    path('', include(router.urls))
]