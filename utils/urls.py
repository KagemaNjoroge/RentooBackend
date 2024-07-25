from rest_framework.routers import DefaultRouter
from .views import TemporaryFileViewSet

router = DefaultRouter()
router.register(r"temporary-files", TemporaryFileViewSet)
urlpatterns = router.urls
