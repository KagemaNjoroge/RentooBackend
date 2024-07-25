from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, PaymentMethodViewSet, MpesaPaymentSettingsViewSet

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payments")
router.register(f"payment-methods", PaymentMethodViewSet, basename="payment_methods")
router.register(
    r"mpesa-payment-settings",
    MpesaPaymentSettingsViewSet,
    basename="mpesa_payment_settings",
)


urlpatterns = router.urls
