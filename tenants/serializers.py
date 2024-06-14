from rest_framework import serializers
from .models import Tenant, Lease, Payment


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'


class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
