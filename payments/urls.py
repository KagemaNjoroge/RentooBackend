from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, PaymentMethodViewSet

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payments")
router.register(f"payment-methods", PaymentMethodViewSet, basename="payment_methods")


urlpatterns = router.urls
