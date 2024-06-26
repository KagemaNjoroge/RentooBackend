from rest_framework import viewsets

from .models import Lease, Payment
from .serializers import LeaseSerializer, PaymentSerializer


class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
