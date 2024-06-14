from .models import Landlord
from .serializers import LandlordSerializer
from rest_framework import viewsets


class LandlordViewSet(viewsets.ModelViewSet):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

