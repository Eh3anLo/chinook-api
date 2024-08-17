from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TrackSerializer, AlbumSerializer, ArtistSerializer
from .models import Track, Album, Artist

from .utils import api_paginator
# Create your views here.


class TrackListView(APIView):
    def get(self, request):
        track_queryset = Track.objects.all().select_related('album','genre','media_type')
        genre = request.query_params.get('genre', None)

        if genre:
            track_queryset = track_queryset.filter(genre__name=genre)    
        if not track_queryset.exists():
            return Response({f"No track found in genre {genre}"}, status=status.HTTP_404_NOT_FOUND)

        paginated_query = api_paginator(track_queryset, request.query_params)
        serializer = TrackSerializer(instance=paginated_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().select_related('artist')
    serializer_class = AlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('artist_id')
    serializer_class = ArtistSerializer
    