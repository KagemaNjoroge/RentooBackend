from rest_framework import viewsets
from .models import TemporaryFile
from .serializers import TemporaryFileSerializer


class TemporaryFileViewSet(viewsets.ModelViewSet):
    queryset = TemporaryFile.objects.all()
    serializer_class = TemporaryFileSerializer
