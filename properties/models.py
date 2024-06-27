from django.db import models

from authentication.models import CustomUser


class Amenity(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=300, default="")
    number = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"


class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    agent = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="properties",
        null=True,
        blank=True,
    )
    photos = models.ManyToManyField(
        "EntityPhoto", related_name="properties", blank=True
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    landlord = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="landlord_properties",
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
    amenities = models.ManyToManyField("Amenity", related_name="amenities", blank=True)
    photos = models.ManyToManyField("EntityPhoto", related_name="houses", blank=True)
    house_number = models.CharField(max_length=50)
    number_of_rooms = models.IntegerField()
    number_of_bedrooms = models.IntegerField(default=0)
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


class EntityPhoto(models.Model):

    image = models.ImageField(upload_to="house_photos/")
    caption = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "House Photo"
        verbose_name_plural = "House Photos"
