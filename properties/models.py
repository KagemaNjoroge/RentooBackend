from django.db import models

from landlords.models import Landlord


class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    agent = models.ForeignKey(
        "agents.Agent",
        on_delete=models.CASCADE,
        related_name="properties",
        null=True,
        blank=True,
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    landlord = models.ForeignKey(
        Landlord,
        on_delete=models.CASCADE,
        related_name="properties",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"


class House(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="houses"
    )
    house_number = models.CharField(max_length=50)
    number_of_rooms = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("property", "house_number")
        verbose_name = "House"
        verbose_name_plural = "Houses"

    def __str__(self):
        return f"House {self.house_number} - {self.property.name}"


class PropertyPhoto(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="photos"
    )
    image = models.ImageField(upload_to="property_photos/")
    caption = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property.name} Photo"

    class Meta:
        verbose_name = "Property Photo"
        verbose_name_plural = "Property Photos"


class HousePhoto(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="house_photos/")
    caption = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"House {self.house.house_number} Photo"

    class Meta:
        verbose_name = "House Photo"
        verbose_name_plural = "House Photos"
