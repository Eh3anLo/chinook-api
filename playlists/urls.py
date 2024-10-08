from django.urls import path
from . import views
urlpatterns = [
    path('', views.PlaylistListApiView.as_view(), name='playlist-list'),
    path('<int:pk>/', views.PlaylistRetreiveApiView.as_view(), name='playlist'),
    path('<int:pk>/tracks/', views.PlaylistTrackApiView.as_view(), name='playlist-add-track'),
    path('<int:p_pk>/tracks/<int:t_pk>/', views.PlaylistTrackDeleteApiView.as_view(), name='playlist-delete-track'),
]


