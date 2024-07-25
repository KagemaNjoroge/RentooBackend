from rest_framework import viewsets
from .serializers import (
    Payment,
    PaymentSerializer,
    PaymentMethodSerializer,
    PaymentMethod,
    MpesaPaymentSettingsSerializer,
    MpesaPaymentSettings,
)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class MpesaPaymentSettingsViewSet(viewsets.ModelViewSet):
    queryset = MpesaPaymentSettings.objects.all()
    serializer_class = MpesaPaymentSettingsSerializer
