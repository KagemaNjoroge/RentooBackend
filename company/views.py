from rest_framework import viewsets
from .serializers import (
    Company,
    CompanySerializer,
    MailSettings,
    MailSettingsSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MailSettingsViewSet(viewsets.ModelViewSet):
    queryset = MailSettings.objects.all()
    serializer_class = MailSettingsSerializer
