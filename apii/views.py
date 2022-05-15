import imp
from pyexpat import model
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import movie
from .serializers import movieSerializer

class movieList(generics.ListCreateAPIView):

    queryset = movie.objects.all()
    serializer_class = movieSerializer


class movieDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = movie.objects.all()
    serializer_class = movieSerializer

