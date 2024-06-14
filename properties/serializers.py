from rest_framework import serializers
from .models import Property, House, PropertyPhoto, HousePhoto


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class PropertyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyPhoto
        fields = '__all__'


class HousePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePhoto
        fields = '__all__'
