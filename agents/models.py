from django.db import models


# Create your models here.
class Agent(models.Model):
    user = models.OneToOneField('authentication.CustomUser', on_delete=models.CASCADE, related_name='agent')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'
        ordering = ['user__username']
