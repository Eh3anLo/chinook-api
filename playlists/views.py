from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from track.models import Track
from .serializers import PlaylistSerializer, PlaylistCreateSerializer
from .models import PlaylistTrack, Playlist
# Create your views here.

class PlaylistRetreiveApiView(APIView):

    def get(self, request , pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, reqeust, pk):
        playlist = Playlist.objects.filter(pk=pk).delete()
        if playlist[0] >= 1:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail" : "No such playlist found"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        print(request.data)
        serializer = PlaylistCreateSerializer(instance=playlist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



class PlaylistListApiView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistCreateSerializer




