from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet
from rest_framework import status
router = DefaultRouter()
router.register("company", CompanyViewSet, basename="company")


urlpatterns = router.urls
