from django.db import models
from tenants.models import Lease


class VacationNotice(models.Model):
    lease = models.ForeignKey(
        Lease, on_delete=models.CASCADE, related_name="vacation_notices"
    )
    notice_date = models.DateTimeField(auto_now_add=True)
    vacation_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"Vacation Notice: {self.lease.tenant} - {self.lease.house}"

    class Meta:
        ordering = ["-notice_date"]
        verbose_name = "Vacation Notice"
        verbose_name_plural = "Vacation Notices"
