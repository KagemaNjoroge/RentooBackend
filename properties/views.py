from django.shortcuts import render
from .serializers import PropertySerializer, HouseSerializer, PropertyPhotoSerializer, HousePhotoSerializer
from .models import Property, House, PropertyPhoto, HousePhoto
from rest_framework import viewsets


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class PropertyPhotoViewSet(viewsets.ModelViewSet):
    queryset = PropertyPhoto.objects.all()
    serializer_class = PropertyPhotoSerializer


class HousePhotoViewSet(viewsets.ModelViewSet):
    queryset = HousePhoto.objects.all()
    serializer_class = HousePhotoSerializer
