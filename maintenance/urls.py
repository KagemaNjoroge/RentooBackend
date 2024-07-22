from rest_framework.routers import DefaultRouter

from .views import MaintenanceRequestViewSet, MaintainerViewSet, MaintenanceViewSet

router = DefaultRouter()
router.register(
    r"maintenance-request", MaintenanceRequestViewSet, basename="maintenance_requests"
)
router.register(r"maintainers", MaintainerViewSet, basename="maintainers")
router.register(r"maintenance", MaintenanceViewSet, basename="maintenance")

urlpatterns = router.urls
