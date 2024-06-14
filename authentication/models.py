from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )
    website = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    kra_pin = models.CharField(max_length=11, null=True, blank=True)

    def is_tenant(self):
        return hasattr(self, "tenant")

    def is_agent(self):
        return hasattr(self, "agent")

    def is_landlord(self):
        return hasattr(self, "landlord")
