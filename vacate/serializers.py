from rest_framework import serializers
from .models import VacationNotice


class VacationNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationNotice
        fields = "__all__"
