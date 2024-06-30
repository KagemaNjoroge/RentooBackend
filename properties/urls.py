from rest_framework.routers import DefaultRouter

from .views import HouseViewSet, PropertyViewSet, EntityPhotoViewSet, UnitViewSet

app_name = "properties"

router = DefaultRouter()
router.register("units", UnitViewSet, basename="units")
router.register("houses", HouseViewSet, basename="houses")
router.register("", PropertyViewSet, basename="properties")
router.register("photos", EntityPhotoViewSet, basename="photos")


urlpatterns = router.urls
