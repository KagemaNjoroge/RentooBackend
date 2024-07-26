from .views import property_stats, property_houses
from django.urls import path


urlpatterns = [
    path("property-stats/", property_stats, name="property_stats"),
    path("property/<int:id>/", property_houses),
]
