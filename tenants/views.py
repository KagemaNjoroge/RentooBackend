from django.shortcuts import render
from .serializers import TenantSerializer, LeaseSerializer, PaymentSerializer
from .models import Tenant, Lease, Payment
from rest_framework import viewsets


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

