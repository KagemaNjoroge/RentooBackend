from rest_framework.routers import DefaultRouter
from .views import AgentsViewSet


router = DefaultRouter()
router.register("agents", AgentsViewSet, basename="agents")

urlpatterns = router.urls
