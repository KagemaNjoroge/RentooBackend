from rest_framework.routers import DefaultRouter
from .views import PropertyCareTakerViewSet

router = DefaultRouter()
router.register(
    r"property-caretaker",
    PropertyCareTakerViewSet,
    basename="propertycaretaker",
)


urlpatterns = []


urlpatterns += router.urls
