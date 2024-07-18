from django.db import models


class Property(models.Model):
    purposes = (
        ("RESIDENTIAL", "Residential"),
        ("COMMERCIAL", "Commercial"),
        ("OTHER", "Other"),
    )
    purpose = models.CharField(
        choices=purposes, default="RESIDENTIAL", blank=True, null=True, max_length=30
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    photos = models.ManyToManyField(
        "EntityPhoto", related_name="properties", blank=True
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"


class House(models.Model):
    purposes = (
        ("RESIDENTIAL", "Residential"),
        ("COMMERCIAL", "Commercial"),
        ("OTHER", "Other"),
    )
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="houses"
    )
    purpose = models.CharField(
        choices=purposes, default="RESIDENTIAL", blank=True, null=True, max_length=30
    )

    photos = models.ManyToManyField("EntityPhoto", related_name="houses", blank=True)
    house_number = models.CharField(max_length=50)
    number_of_rooms = models.IntegerField(default=1)
    number_of_bedrooms = models.IntegerField(default=0)
    is_occupied = models.BooleanField(default=False)
    rent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(
        blank=True, null=True, default="No additional description"
    )

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


class Unit(models.Model):
    property = models.ForeignKey(to=Property, on_delete=models.CASCADE)
    unit_name = models.CharField(max_length=50)
    floor = models.CharField(max_length=30)
    houses = models.ManyToManyField(to=House)

    def __str__(self) -> str:
        return self.unit_name

    class Meta:
        verbose_name = "Property Unit"
        verbose_name_plural = "Property Units"
