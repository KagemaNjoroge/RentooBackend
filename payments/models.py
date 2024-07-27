from django.db import models
from tenants.models import Lease


class PaymentMethod(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"


class Payment(models.Model):
    status = (
        ("In progress", "In progress"),
        ("Complete", "Complete"),
        ("Cancelled", "Cancelled"),
    )
    payment_status = models.CharField(
        choices=status, default="In progress", max_length=30
    )
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reference_code = models.CharField(max_length=30, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment: {self.lease} - {self.amount}"

    class Meta:
        ordering = ["-payment_date"]
        verbose_name = "Payment"
        verbose_name_plural = "Payments"


class MpesaPaymentSettings(models.Model):
    consumer_key = models.CharField(max_length=100)
    consumer_secret = models.CharField(max_length=100)
    pass_key = models.CharField(max_length=100)
    short_code = models.CharField(max_length=100)
    test_mode = models.BooleanField(default=True)

    def __str__(self):
        return "Mpesa Payment Settings"

    class Meta:
        verbose_name = "Mpesa Payment Settings"
        verbose_name_plural = "Mpesa Payment Settings"
