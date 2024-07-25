from rest_framework import serializers
from .models import Company, MailSettings


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class MailSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailSettings
        fields = "__all__"
