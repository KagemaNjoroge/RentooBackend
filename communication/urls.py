from rest_framework.routers import DefaultRouter

from .views import MessageViewSet, NotificationViewSet

router = DefaultRouter()
router.register("messages", MessageViewSet, basename="messages")
router.register("notifications", NotificationViewSet, basename="notifications")

urlpatterns = router.urls
