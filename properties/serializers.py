from rest_framework import serializers
from .models import Property, House, EntityPhoto, Unit


class EntityPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityPhoto
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = "__all__"
