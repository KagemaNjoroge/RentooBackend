from django.shortcuts import render
from .serializers import (
    EntityPhotoSerializer,
    PropertySerializer,
    HouseSerializer,
)
from .models import Property, House, EntityPhoto
from rest_framework import viewsets


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class EntityPhotoViewSet(viewsets.ModelViewSet):
    queryset = EntityPhoto.objects.all()
    serializer_class = EntityPhotoSerializer
