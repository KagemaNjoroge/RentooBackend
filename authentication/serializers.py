from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "is_active": {"read_only": True},
            "is_supeuser": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_superuser": {"read_only": True},
            "last_login": {"read_only": True},
            "date_joined": {"read_only": True},
            "groups": {"write_only": True},
            "user_permissions": {"write_only": True},
        }


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField()
