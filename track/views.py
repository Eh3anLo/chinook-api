from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from rest_framework import status, viewsets , generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TrackSerializer, TrackCreateSerializer, AlbumSerializer, ArtistSerializer
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
    
    def post(self, request):
        serializer = TrackCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class TrackRetreiveUpdateDestroyApiView(APIView):
    def get(self, request, pk):
        track = get_object_or_404(Track.objects.select_related('album','genre','media_type'), pk=pk)
        serializer = TrackSerializer(instance = track)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        track = Track.objects.filter(pk=pk).delete()
        if track[0] >= 1:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail" : "No such track exist"},status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk):
        track = get_object_or_404(Track.objects.select_related('album','genre','media_type'), pk=pk)
        serializer = TrackCreateSerializer(instance=track, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)








class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.select_related('artist').all()
    serializer_class = AlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('artist_id')
    serializer_class = ArtistSerializer
    