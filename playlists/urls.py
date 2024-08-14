from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.PlaylistApiView.as_view(), name='playlist')
]