from rest_framework import viewsets
from .models import VacationNotice
from .serializers import VacationNoticeSerializer


class VacationNoticeViewSet(viewsets.ModelViewSet):
    queryset = VacationNotice.objects.all()
    serializer_class = VacationNoticeSerializer
