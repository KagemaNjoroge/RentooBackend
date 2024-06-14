from django.urls import path
from rest_framework.routers import DefaultRouter

from .login import LoginView
from .views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = router.urls
urlpatterns += [
    path("login/", LoginView.as_view(), name="login"),
]
