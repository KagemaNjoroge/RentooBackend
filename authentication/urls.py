from django.urls import path
from rest_framework.routers import DefaultRouter

from .login import login
from .views import UserViewSet

app_name = "authentication"


router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = router.urls
urlpatterns += [
    path("login/", login, name="login"),
]
