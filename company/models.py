from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["name"]
