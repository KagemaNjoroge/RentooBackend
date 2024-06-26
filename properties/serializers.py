from rest_framework import serializers
from .models import Property, House, EntityPhoto


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"


class EntityPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityPhoto
        fields = "__all__"
