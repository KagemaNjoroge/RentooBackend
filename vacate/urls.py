from django.db import router
from .views import VacationNoticeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"vacation-notices", VacationNoticeViewSet)
urlpatterns = router.urls
