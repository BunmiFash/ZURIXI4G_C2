from django.shortcuts import render
from rest_framework import generics
from musicapp.serializers import SongSerializer, ArtisteSerializer
from musicapp.models import Song, Artiste
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.

# Lists all Songs
class ListSongs(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


# Lists all Artistes
class ListArtists(generics.ListAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer  

# Get a particular Song    
class GetOneSong(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# Update a particular song
class UpdateSong(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'id'

#Deleting a particular song
class DeleteSong(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'id'

# class DeleteSong(APIView):

#     def delete(self, request):
#         delete_song = Song.objects.all()
#         delete_song.delete()
#         return JsonResponse({'data': f'{delete_song.title}' "is successfully deleted"})



