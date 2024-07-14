from django.db import models
from authentication.models import CustomUser
from properties.models import House


class Tenant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="tenants/", blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    houses = models.ManyToManyField(House, verbose_name="houses", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"


class Lease(models.Model):
    tenant = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="leases"
    )
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="leases")
    start_date = models.DateField()
    end_date = models.DateField()
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    renew_monthly = models.BooleanField(default=True)

    def __str__(self):
        return f"Lease: {self.tenant} - {self.house}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Lease"
        verbose_name_plural = "Leases"
