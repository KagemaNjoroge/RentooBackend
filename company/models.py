from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(blank=True, null=True)

    # extra settings -> language, currency
    language = models.CharField(max_length=100, default="en")
    currency = models.CharField(max_length=100, default="KES")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["name"]


class MailSettings(models.Model):
    port = models.IntegerField()
    smtp_server = models.CharField(max_length=30)
    use_tls = models.BooleanField(default=False)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=50, default="default server")
    description = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    # def save(self, *args, **kwargs) -> None:
    #     # TODO: hash password
    #     return super().save(args, kwargs)

    class Meta:
        verbose_name = "Mail Settings"
        verbose_name_plural = "Mail Settings"
