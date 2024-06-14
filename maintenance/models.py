from django.db import models

from properties.models import Property


class MaintenanceRequest(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="maintenance_requests"
    )
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
