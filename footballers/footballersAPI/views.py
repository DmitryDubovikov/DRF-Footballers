from django.shortcuts import render
from rest_framework import generics
from .models import Footballer
from .serializers import FootballerSerializer

# Create your views here.

    
class FootballerAPIList(generics.ListCreateAPIView):
    '''
    Provides get and post method handlers.
    '''
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer
    
        
class FootballerAPUpdate(generics.UpdateAPIView):
    '''
    Provides put and patch method handlers.
    '''
    queryset = Footballer.objects.all()  # NB: queries are lazy, thus all() is ok
    serializer_class = FootballerSerializer
    
    
class FootballerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Used for read-write-delete endpoints to represent a single model instance.
    Provides get, put, patch and delete method handlers.
    '''
    queryset = Footballer.objects.all()  # NB: queries are lazy, thus all() is ok
    serializer_class = FootballerSerializer
