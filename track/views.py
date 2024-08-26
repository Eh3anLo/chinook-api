from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.core.paginator import Paginator
from rest_framework import status, viewsets , generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TrackSerializer, TrackCreateSerializer, AlbumSerializer, ArtistSerializer, GenreSerializer, MediaTypeSerializer
from .models import Track, Album, Artist, Genre, MediaType

from .tasks import bulk_upload_json_data
from .utils import api_paginator
import json
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)



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
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class TrackSearchApiView(APIView):
    def get(self, request):

        query = request.query_params.get('query')
        src_type = request.query_params.get('type',"plain")
        req_field = request.query_params.get('fields')

        search_field = ["name","media_type__name","genre__name","composer","album__title"]
        search_query = SearchQuery(query,search_type=src_type)

        if req_field:
            search_field = req_field.split(",")

        if src_type == "raw":
            query = "|".join(query.split(' '))

        tracks = Track.objects.annotate(
            search=SearchVector(*search_field),
        ).filter(search=search_query).select_related('album','genre','media_type')

        paginated_query = api_paginator(tracks, request.query_params)
        serializer = TrackSerializer(paginated_query, many=True)

        
        data = {
            "Keyword": query,
            "results": serializer.data
        }

        return Response(data)

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.select_related('artist').all()
    serializer_class = AlbumSerializer



class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('artist_id')
    serializer_class = ArtistSerializer


    
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



class MediaTypeViewSet(viewsets.ModelViewSet):
    queryset = MediaType.objects.all()
    serializer_class = MediaTypeSerializer



class TrackBulkUpload(APIView):
    def post(self, request):
        json_data = json.load(request.FILES.get('tracks'))
        res = bulk_upload_json_data.apply_async(args=[json_data])
        if json_data:
            return Response({"message" : res.state }, status=status.HTTP_201_CREATED)        
