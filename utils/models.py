from django.db import models


# TODO: create a cron job to delete temporary images every day at midnight
class TemporaryFile(models.Model):
    file = models.FileField(upload_to="temporary_files/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url

    class Meta:
        ordering = ["-created_at"]
