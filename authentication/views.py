from rest_framework import viewsets

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    # override to  also create a password for the user
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
