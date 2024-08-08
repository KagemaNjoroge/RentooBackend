from django.db import models

from properties.models import House


class MaintenanceRequest(models.Model):
    maintenance_status = (
        ("In Progress", "In Progress"),
        ("Scheduled", "Scheduled"),
        ("Pending", "Pending"),
        ("Complete", "Complete"),
    )
    status = models.CharField(
        max_length=30, choices=maintenance_status, default="Pending"
    )
    house = models.ForeignKey(to=House, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Maintenance Request for {self.house}"

    class Meta:
        ordering = ["-request_date"]
        verbose_name = "Maintenance Request"
        verbose_name_plural = "Maintenance Requests"


class Maintainer(models.Model):
    maintainer_types = (("Individual", "Individual"), ("Company", "Company"))
    maintainer_type = models.CharField(
        choices=maintainer_types, max_length=30, default="Individual"
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Maintainer"
        verbose_name_plural = "Maintainers"


class Maintenance(models.Model):
    request = models.ForeignKey(to=MaintenanceRequest, on_delete=models.CASCADE)
    maintainer = models.ForeignKey(to=Maintainer, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_done = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)  # to track in expenses

    def __str__(self) -> str:
        return f"Maintenance for {self.request.id}"

    class Meta:
        verbose_name = "Maintenance"
        verbose_name_plural = "Maintenances"
        ordering = ["-date_done"]

    def save(
        self,
    ) -> None:
        # mark the maintenance request as complete if is_done
        if self.is_done:
            self.request.is_completed = True
            self.request.status = "Complete"
            self.request.save()

        return super().save()
