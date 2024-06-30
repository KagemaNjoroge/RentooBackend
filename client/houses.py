from django.shortcuts import render
from properties.models import Property, House
from django.shortcuts import get_object_or_404


def houses(request):
    houses = House.objects.all()
    return render(request, "houses/index.html", context={"houses": houses})


def house_details(request, id):
    house = get_object_or_404(House, id=id)
    return render(request, "houses/house-details.html", context={"house": house})


def new_house(request):
    props = Property.objects.all()
    house_types = []
    for i in House.purpose.field.choices:
        house_types.append({"name": i[-1], "value": i[0]})
    return render(
        request,
        "houses/new.html",
        context={"properties": props, "house_types": house_types},
    )
