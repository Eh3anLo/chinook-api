from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from track.models import Track
from .serializers import PlaylistSerializer
from .models import PlaylistTrack, Playlist
# Create your views here.

class PlaylistApiView(APIView):

    def get(self, request , pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        serializer = PlaylistSerializer(playlist)

        return Response(serializer.data, status=status.HTTP_200_OK)

