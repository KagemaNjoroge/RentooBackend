from rest_framework.routers import DefaultRouter

from .views import HouseViewSet, PropertyViewSet, EntityPhotoViewSet

router = DefaultRouter()
router.register("houses", HouseViewSet, basename="houses")
router.register("", PropertyViewSet, basename="properties")
router.register("photos", EntityPhotoViewSet, basename="photos")


urlpatterns = router.urls
