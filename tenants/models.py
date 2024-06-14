from django.db import models
from authentication.models import CustomUser
from properties.models import House


class Tenant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='tenant', null=True, blank=True)

    class Meta:
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'


class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='leases')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='leases')
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Lease: {self.tenant} - {self.house}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Lease'
        verbose_name_plural = 'Leases'


class Payment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Payment: {self.lease} - {self.amount}'
