from rest_framework import serializers
from .models import Payment, PaymentMethod, MpesaPaymentSettings


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class MpesaPaymentSettingsSerializer(serializers.ModelSerializer):
    # consumer_key = serializers.CharField(write_only=True)
    # consumer_secret = serializers.CharField(write_only=True)
    # pass_key = serializers.CharField(write_only=True)

    class Meta:
        model = MpesaPaymentSettings
        fields = "__all__"
