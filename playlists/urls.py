from django.urls import path
from . import views
urlpatterns = [
    path('', views.PlaylistListApiView.as_view(), name='playlist-list'),
    path('<int:pk>/', views.PlaylistRetreiveApiView.as_view(), name='playlist'),
]


