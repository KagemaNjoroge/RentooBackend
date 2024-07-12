from .models import PropertyCareTaker
from rest_framework import serializers


class PropertyCareTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyCareTaker
        fields = "__all__"
