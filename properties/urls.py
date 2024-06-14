from rest_framework.routers import DefaultRouter

from .views import (
    HouseViewSet,
    PropertyViewSet,
    PropertyPhotoViewSet,
    HousePhotoViewSet,
)

router = DefaultRouter()
router.register("houses", HouseViewSet, basename="houses")
router.register("", PropertyViewSet, basename="properties")
router.register("property_photos", PropertyPhotoViewSet, basename="property_photos")
router.register("house_photos", HousePhotoViewSet, basename="house_photos")

urlpatterns = router.urls
