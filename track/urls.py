from django.urls import path
from . import views
urlpatterns = [
    path('', views.TrackListView.as_view(), name="track-list")
]