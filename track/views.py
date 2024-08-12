from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TrackSerializer, AlbumSerializer
from .models import Track, Album
# Create your views here.


class TrackListView(APIView):
    def get(self, request):
        track_queryset = Track.objects.all().select_related('album','genre','media_type')
        genre = request.query_params.get('genre', None)
        if genre:
            track_queryset = track_queryset.filter(genre__name=genre)[:10]
            
        if not track_queryset.exists():
            return Response({f"No track found in genre {genre}"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TrackSerializer(track_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class AlbumListView(APIView):
    def get(self, request):
        album_queryset = Album.objects.all()
        serializer = AlbumSerializer(album_queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
