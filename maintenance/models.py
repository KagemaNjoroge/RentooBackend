from django.db import models

from properties.models import House, Property


class MaintenanceRequest(models.Model):
    house = models.ForeignKey(to=House, on_delete=models.CASCADE, null=True, blank=True)

    description = models.TextField()
    requested_by = models.ForeignKey(
        "authentication.CustomUser", on_delete=models.CASCADE
    )
    request_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Maintenance Request for {self.property}"

    class Meta:
        ordering = ["-request_date"]
        verbose_name = "Maintenance Request"
        verbose_name_plural = "Maintenance Requests"
