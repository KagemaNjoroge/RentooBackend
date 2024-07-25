from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, MailSettingsViewSet

router = DefaultRouter()
router.register(r"company", CompanyViewSet, basename="company")
router.register(r"mail-settings", MailSettingsViewSet, basename="mail_settings")


urlpatterns = router.urls
