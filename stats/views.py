from properties.models import Property, House
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def property_stats(request):
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
