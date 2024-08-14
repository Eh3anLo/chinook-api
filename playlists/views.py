from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from track.models import Track
from .serializers import PlaylistSerializer
from .models import PlaylistTrack
# Create your views here.

class PlaylistApiView(APIView):

    def get(self, request , pk):
        playlist_queryset = PlaylistTrack.objects.filter(pk=pk).prefetch_related('track')
        serializer = PlaylistSerializer(playlist_queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

