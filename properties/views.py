from .serializers import (
    EntityPhotoSerializer,
    PropertySerializer,
    HouseSerializer,
    UnitSerializer,
)
from .models import Property, House, EntityPhoto, Unit
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    @swagger_auto_schema(
        operation_summary="Get all properties",
        operation_description="Get all properties from the database",
    )
    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class EntityPhotoViewSet(viewsets.ModelViewSet):
    queryset = EntityPhoto.objects.all()
    serializer_class = EntityPhotoSerializer
