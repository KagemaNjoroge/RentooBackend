from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to="agents/", blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"
        ordering = ["name"]
