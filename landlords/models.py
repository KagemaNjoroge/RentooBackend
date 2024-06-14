from django.db import models
from authentication.models import CustomUser


class Landlord(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Landlord'
        verbose_name_plural = 'Landlords'
