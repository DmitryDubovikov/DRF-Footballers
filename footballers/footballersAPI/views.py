from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Footballer, Country
from .serializers import FootballerSerializer

# Create your views here.

class FootballerViewSet(viewsets.ModelViewSet):
    queryset = Footballer.objects.all()  # NB: queries are lazy, thus all() is ok
    serializer_class = FootballerSerializer
    
    def get_queryset(self):
        # here we can redefine queryset
        # return Footballer.objects.all()[:2]
        pk = self.kwargs.get('pk')
        if pk:
            Footballer.objects.filter(pk=pk)
        return Footballer.objects.all()
    
    
    @action(methods=['get'], detail=False)
    def countries(self, request):
        # adds endpoint http://127.0.0.1:8000/api/v1/footballers/countries
        queryset = Country.objects.all() 
        return Response({'countries': [c.name for c in queryset]})
    
    
    @action(methods=['get'], detail=True)
    def country(self, request, pk=None):
        # adds endpoint http://127.0.0.1:8000/api/v1/footballers/1/country/
        queryset = Country.objects.get(pk=pk) 
        return Response({'country': queryset.name})
    
    
# class FootballerAPIList(generics.ListCreateAPIView):
#     '''
#     Provides get and post method handlers.
#     '''
#     queryset = Footballer.objects.all()
#     serializer_class = FootballerSerializer
    
        
# class FootballerAPUpdate(generics.UpdateAPIView):
#     '''
#     Provides put and patch method handlers.
#     '''
#     queryset = Footballer.objects.all()  # NB: queries are lazy, thus all() is ok
#     serializer_class = FootballerSerializer
    
    
# class FootballerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     '''
#     Used for read-write-delete endpoints to represent a single model instance.
#     Provides get, put, patch and delete method handlers.
#     '''
#     queryset = Footballer.objects.all()  # NB: queries are lazy, thus all() is ok
#     serializer_class = FootballerSerializer
