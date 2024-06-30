from django.shortcuts import render
from properties.models import Property
from django.shortcuts import get_object_or_404


def new_property(request):
    return render(request, "property/new.html")


def property(request):
    properties = Property.objects.all()
    return render(request, "property/index.html", context={"property": properties})


def property_details(request, id):
    prop = get_object_or_404(Property, id=id)

    return render(request, "property/property-details.html", context={"property": prop})
