from rest_framework import serializers
from .models import TemporaryFile


class TemporaryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryFile
        fields = "__all__"
