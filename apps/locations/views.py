from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from .serializers import LocationBaseSerializer, LocationCreateSerializer
from .models import Location
from drf_spectacular.utils import extend_schema
# Create your views here.

app_name = "locations"


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationBaseSerializer

    # @extend_schema(
    #         request=LocationCreateSerializer, 
    #         responses={201: LocationBaseSerializer}, 
    #         methods=['POST']
    # )
    # def create_location(self):
    #     return []


    # @extend_schema(
    #         responses={201: LocationBaseSerializer}, 
    #         methods=['GET']
    # )
    # def get_location(self):
    #     return self.queryset
    
    # @extend_schema(
    #         request=LocationCreateSerializer, 
    #         responses={201: LocationBaseSerializer}, 
    #         methods=['PUT']
    # )
    # def update_location(self, request):
    #     print(request)
    #     pass
