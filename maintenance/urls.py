from rest_framework.routers import DefaultRouter

from .views import MaintenanceRequestViewSet

router = DefaultRouter()
router.register(
    r"maintenance", MaintenanceRequestViewSet, basename="maintenance_requests"
)

urlpatterns = router.urls
