from django.db import models
from properties.models import Property


class PropertyCareTaker(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="caretakers",
        blank=True,
        null=True,
    )
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="property_care_takers/", blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Property Care Taker"
        verbose_name_plural = "Property Care Takers"
