from rest_framework import serializers
from properties.serializers import HouseSerializer
from .models import Lease, Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"


class LeaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lease
        fields = "__all__"
