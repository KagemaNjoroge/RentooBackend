from .views import property_stats
from django.urls import path


urlpatterns = [
    path("property-stats/", property_stats, name="property_stats"),
]
