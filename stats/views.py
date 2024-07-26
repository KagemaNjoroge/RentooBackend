from properties.models import Property, House
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import get_object_or_404

from properties.serializers import HouseSerializer


@api_view(["GET"])
def property_stats(request: Request):
    """
    Returns the number of properties,
    houses, occupied and unoccupied houses
    in the system
    """
    properties = Property.objects.all()
    property_count = properties.count()
    house_count = House.objects.all().count()
    # unnoccupied houses
    vacant_houses = House.objects.filter(is_occupied=False).count()
    return Response(
        {
            "property_count": property_count,
            "house_count": house_count,
            "vacant_houses": vacant_houses,
            "occupied_houses": house_count - vacant_houses,
        }
    )


@api_view(["GET"])
def property_houses(request: Request, id: int):
    property = get_object_or_404(Property, id=id)
    houses = House.objects.filter(property=property)
    serializer = HouseSerializer(houses, many=True)
    count = houses.count()
    
    return Response(serializer.data)
