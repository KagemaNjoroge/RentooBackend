from .models import PropertyCareTaker
from rest_framework import viewsets
from .serializers import PropertyCareTakerSerializer


class PropertyCareTakerViewSet(viewsets.ModelViewSet):
    queryset = PropertyCareTaker.objects.all()
    serializer_class = PropertyCareTakerSerializer
