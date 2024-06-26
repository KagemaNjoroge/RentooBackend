from rest_framework.routers import DefaultRouter

from .views import LeaseViewSet, PaymentViewSet

router = DefaultRouter()

router.register(r"leases", LeaseViewSet, basename="leases")
router.register(r"payments", PaymentViewSet, basename="payments")

urlpatterns = router.urls
