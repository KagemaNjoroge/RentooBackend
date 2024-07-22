from rest_framework import viewsets

from .models import MaintenanceRequest, Maintainer, Maintenance
from .serializers import (
    MaintenanceRequestSerializer,
    MaintainerSerializer,
    MaintenanceSerializer,
)


class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer


class MaintainerViewSet(viewsets.ModelViewSet):
    queryset = Maintainer.objects.all()
    serializer_class = MaintainerSerializer


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintainerSerializer
